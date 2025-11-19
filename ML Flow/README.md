## 1. What is MLflow and where it sits

**MLflow** is an open-source platform to manage the machine-learning lifecycle: experiment tracking, model versioning, deployment and serving. ([anderfernandez.com][1])
It has three major components:

* **Tracking** – logs runs (parameters, metrics, artifacts) ([MLflow][2])
* **Projects** – packaging reproducible code (optional) ([anderfernandez.com][1])
* **Models + Model Registry** – versioning and lifecycle of models (staging, production) ([anderfernandez.com][1])
  In an MLOps context it sits at the intersection of experimentation & production: you use it during development (tracking) and also for governance and deployment (model registry).

---

## 2. Setup (Installation + Server + Backend)

When someone asks **“how did you set it up?”**, you’ll want to explain both your local/dev setup and the production/centralised server setup.

### a) Local/Dev setup (quick start)

Code snippet:

```bash
pip install mlflow
```

In Python:

```python
import mlflow
mlflow.set_experiment("my_experiment")
```

Then train a model and log:

```python
import mlflow.sklearn
# enable autolog
mlflow.sklearn.autolog()

# train model
model.fit(X_train, y_train)
```

Then launch UI:

```bash
mlflow ui --port 5000
```

This logs to a local folder by default. ([MLflow][2])

### b) Centralised/Production Tracking Server

For team usage, you deploy a tracking server with:

* Backend store (database) – e.g., Postgres, MySQL, SQLite for small. ([anderfernandez.com][1])
* Artifact store – where models and large files go (S3, GCS, Azure Blob, local FS) ([anderfernandez.com][1])
* Tracking server CLI:

```bash
mlflow server --backend-store-uri postgresql://user:pwd@host/db \
              --default-artifact-root s3://my-bucket/mlflow-artifacts \
              --host 0.0.0.0 --port 5000
```

Then in your code you point:

```python
mlflow.set_tracking_uri("http://<server-host>:5000")
```

And optionally:

```python
mlflow.set_experiment("my_team_project")
```

This allows multiple users/projects to log and share runs. ([anderfernandez.com][1])

### c) Additional details (auth, scaling)

If using cloud host (e.g., Databricks), you’ll configure authentication, environment variables (token, host, etc). ([Databricks Documentation][3])
Also worth noting: isolate environments using conda/venv so logging environments are reproducible. ([Medium][4])

---

## 3. Code Basics / Usage Patterns

When asked how you *used* MLflow in your pipeline, you can describe this pattern:

### Step-by-step

1. **Configure tracking URI & experiment**

   ```python
   import mlflow
   mlflow.set_tracking_uri("http://mlflow-server:5000")
   mlflow.set_experiment("customer_churn_modeling")
   ```
2. **Start a run, log parameters/metrics/artifacts**

   ```python
   with mlflow.start_run():
       mlflow.log_param("model_type", "RandomForest")
       mlflow.log_param("n_estimators", 100)
       model = RandomForestClassifier(n_estimators=100).fit(X_train, y_train)
       y_pred = model.predict(X_test)
       mlflow.log_metric("accuracy", accuracy_score(y_test, y_pred))
       mlflow.sklearn.log_model(model, "rf_model")
   ```

   Or use autolog (for sklearn, pytorch etc):

   ```python
   mlflow.sklearn.autolog()
   model.fit(X_train, y_train)
   ```

   ([MLflow][2])
3. **View runs in UI** – show hyper-parameters, metrics, artifacts.
4. **Model registration / promotion** – after selecting best run, register model:

   ```python
   mlflow.register_model("runs:/<run_id>/rf_model", "ChurnRF")
   ```

   Then promote to production stage (via Model Registry) – tracking versions, staging phases.
5. **Serving / inference** – load model for predictions:

   ```python
   loaded = mlflow.pyfunc.load_model("models:/ChurnRF/1")
   preds = loaded.predict(new_data)
   ```

   Or serve as REST endpoint:

   ```bash
   mlflow models serve -m "models:/ChurnRF/1" -p 1234
   ```

   ([anderfernandez.com][1])

### Key API methods to mention

* `mlflow.set_tracking_uri()`
* `mlflow.set_experiment()` / `mlflow.create_experiment()`
* `mlflow.start_run()` / `mlflow.end_run()`
* `mlflow.log_param()`, `mlflow.log_metric()`, `mlflow.log_artifact()`, `mlflow.log_model()`
* `mlflow.sklearn.autolog()` (or relevant framework)
* `mlflow.register_model()`, `mlflow.pyfunc.load_model()`
* `mlflow.models.serve()`

---

## 4. How it integrates in your MLOps architecture

When explaining end-to-end, you’ll want to show how MLflow connects to other components:

* **Experimentation/dev**: Data scientist uses notebooks/code, logs into MLflow Tracking.
* **Feature store/data pipeline**: Upstream you have data ingestion/cleaning; MLflow doesn’t handle data pipelines per se but can track versions of data/features (via artifacts or tags).
* **Model training & tuning**: MLflow captures runs from hyperparameter sweeps, performance metrics, code versions.
* **Model registry & governance**: Once a model is “approved”, you register it in MLflow Model Registry, tag stage “Staging”, then “Production”. This provides transparency, versioning, audit trail.
* **Deployment / serving**: The registered model can be served via MLflow’s built-in serving or pushed to a dedicated inference layer (e.g., REST microservice) referencing the model URI from MLflow.
* **Monitoring & feedback loop**: After deployment you monitor model performance drift, data drift, resource usage. You can log evaluation metrics back into MLflow or integrate MLflow’s webhooks or custom logging.
* **CI/CD/CT**: Training jobs, model registration, deployment steps are automated in pipelines (e.g., with Jenkins/GitHub Actions/Azure DevOps) which call MLflow APIs to transition model stages.
* **Governance/audit**: Every run has metadata (user, timestamp, parameters, code version, data version) stored in MLflow backend store; artifacts stored separately; you have lineage and reproducibility.

Thus, MLflow acts as a central “knowledge hub” in the MLOps architecture. When asked, you can draw a diagram: data → features → model training (logged in MLflow) → model registry → serving → monitoring → retraining → back to MLflow.

---

## 5. “How I did it” – concise answer for an interviewer/peer

> “I set up an MLflow tracking server with a Postgres backend for metadata and S3 (or GCS) bucket for artifacts, configured our model-training pipeline to point to the MLflow URI, invoked `mlflow.log_param` & `mlflow.log_metric` in each run (and used `autolog` for our sklearn/pytorch steps). After training, we registered the best model in the MLflow Model Registry, marked it as ‘Staging’, ran integration tests, then promoted to ‘Production’. For deployment we loaded the model via MLflow’s pyfunc loader and exposed it as a REST endpoint (or used `mlflow models serve`). All of this gives us full traceability from data + code version → hyper-params → metrics → deployed model version, which feeds into our CI/CD/CT pipeline and enables monitoring + retraining loops.”

You can follow up by showing **specifics**: e.g., “We used `mlflow.set_tracking_uri("http://mlflow.mycompany.com:5000")` in our training script, teams used `mlflow ui` to review experiments, and we integrated with GitHub Actions so that when a model passes tests it triggers `mlflow.transition_model_version_stage(model_name='MyModel', version=2, stage='Production')` via the REST API.”

---

## 6. Best practices / tips

* Use a **dedicated tracking server** for team/production use — avoid default local file logging for production. ([MLflow][5])
* Version your **code, data, and model** so you can reproduce runs. Logging code Git-SHA as a parameter/tag is helpful.
* Use **autolog** where possible to reduce boilerplate.
* Use **Model Registry** to manage lifecycle (development → staging → production).
* Tag runs with meaningful metadata (dataset version, user, branch, experiment type).
* Clean up/archival strategy for old runs, old artifacts.
* Secure access to tracking server, especially if exposing UI externally; use authentication.
* Monitor resources of the server (since artifact storage can grow large).
* Integrate MLflow into your CI/CD pipeline: e.g., after training & evaluation, the pipeline can automatically register and promote the best model.
* Ensure artifact store is scalable and accessible (cloud storage is often preferred).
* Document your experiment/MLflow strategy so non-data scientists (e.g., product owners) can view model versions easily.

---

## 7. Summary: Key things you must be able to explain

* What MLflow does (tracking, model registry, projects)
* How you install and set up (local vs central server)
* How you instrument code to log runs, parameters, metrics, artifacts
* How you set up Model Registry and promote versions
* How you deploy or serve models from MLflow
* How it fits into the larger MLOps workflow (data pipeline → training → deployment → monitoring)
* How you ensure governance, reproducibility, collaboration via MLflow