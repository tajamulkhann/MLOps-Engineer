## 1. What is DVC and where it sits

**DVC (Data Version Control)** is an open-source tool for **versioning datasets, models, and ML pipelines** using a Git-like interface.
It solves the main limitation of Git: **Git cannot store large data, models, or artifacts efficiently** — DVC stores them in remote storage (S3, GCS, Azure, SSH, local remote) while keeping lightweight pointers in Git.

### What DVC provides:

* **Data Versioning** — track large datasets & `.pkl` model artifacts without storing them inside Git.
* **Pipeline Management (`dvc.yaml`)** — define ML workflow stages (ingestion → transform → train → evaluate → deploy).
* **Reproducibility** — one command `dvc repro` re-runs the entire pipeline if any input changes.
* **Remote Storage** — S3, GCS, Azure Blob, SSH, local folder, etc.
* **Experiment Tracking** — DVC `exp` commands for branching experiments.

**Where it sits in MLOps:**
DVC sits **between data engineering & ML training**, handling dataset versions, pipeline orchestration, model storage, and collaboration.

---

## 2. Setup (Installation + Remote Storage + Initialization)

When someone asks **“How did you set up DVC?”**, you should answer like this:

### a) Local/Dev Setup (quick start)

Install:

```bash
pip install dvc
```

Initialize DVC inside your project:

```bash
dvc init
```

This creates:

* `.dvc/` internal metadata
* `.dvcignore`
* Updates `.gitignore`

---

### b) Add data / models to DVC

Example: adding raw data:

```bash
dvc add data/raw/
```

This creates:

* `data/raw.dvc` → pointer file
* Actual data stays in your workspace
* Git now tracks only the pointer, not the heavy data

Commit it:

```bash
git add data/raw.dvc .gitignore
git commit -m "Track raw dataset with DVC"
```

Same for model artifacts:

```bash
dvc add final_model/model.pkl
git add final_model/model.pkl.dvc
git commit -m "Track trained model artifact"
```

---

### c) Configure Remote Storage (S3 / GCS / local)

For S3 remote:

```bash
dvc remote add -d myremote s3://mybucket/dvcstore
dvc remote modify myremote access_key_id <KEY>
dvc remote modify myremote secret_access_key <SECRET>
```

Push data/models to S3:

```bash
dvc push
```

Pull data/models (for new teammates or CI):

```bash
dvc pull
```

---

## 3. Pipeline Basics / Usage Patterns

When an interviewer asks **“How do you define and run ML pipelines with DVC?”**, show this pattern:

### a) Create Pipeline Stages (`dvc.yaml`)

Example pipeline:

```bash
dvc run -n ingest \
    -d data/raw/raw.csv \
    -o data/processed/processed.csv \
    python src/data_ingestion.py
```

Transformation stage:

```bash
dvc run -n transform \
    -d data/processed/processed.csv \
    -o data/features/features.csv \
    python src/data_transformation.py
```

Training stage:

```bash
dvc run -n train \
    -d data/features/features.csv \
    -o final_model/model.pkl \
    python src/model_trainer.py
```

DVC automatically updates `dvc.yaml` and tracks dependencies & outputs.

---

### b) Reproducing the entire pipeline

If any input changes:

```bash
dvc repro
```

This re-runs only the affected stages
(e.g., if new data comes → runs transform + train again).

---

### c) Experiment tracking with DVC

You can run experiments like:

```bash
dvc exp run
```

List experiments:

```bash
dvc exp show
```

Promote experiment to Git:

```bash
dvc exp apply <exp_id>
git commit -am "Promote best experiment"
```

---

## 4. How DVC fits into the MLOps architecture

When explaining this to an interviewer, say:

* **Upstream**: Data ingestion saves raw data → DVC version controls it.
* **Feature engineering**: Transform scripts produce processed data/artifacts → DVC tracks these.
* **Model training**: Output model artifacts (`model.pkl`, preprocessors, scalers) → stored via DVC in S3.
* **Pipeline**: Entire workflow defined in `dvc.yaml`; `dvc repro` executes stages.
* **Collaboration**: Team pulls exactly the same dataset/model with `dvc pull`.
* **CI/CD**: Training runs in GitHub Actions; artifacts pushed to DVC remote.
* **Deployment**: Best model version pulled from DVC and packaged via Docker → pushed to ECR → deployed to EC2.

Essentially, DVC ensures **data + code + model = reproducible always**.

---

## 5. “How I used it in my project” – interview-ready answer

> “I set up DVC to version the entire ML pipeline — raw data, processed data, features, and the final `.pkl` model. Each stage (ingestion → transformation → validation → training → evaluation) was defined in `dvc.yaml`. I added S3 as the DVC remote so all heavy datasets and model artifacts stayed in S3 while only pointer files were stored in Git. Anytime upstream data changed, `dvc repro` triggered only the necessary pipeline stages. I also used DVC experiments to run multiple training trials and promoted the best model. Finally, CI pulled data via DVC, retrained the model, pushed artifacts to S3, and we deployed the final model via Docker → ECR → EC2.”

---

## 6. Best Practices / Tips

* Always use a **cloud remote** (S3/GCS/Azure/SSH).

* Avoid committing the raw data — commit only `.dvc` pointer files.

* Always run:

  ```bash
  dvc push
  git push
  ```

  so Git + DVC stay synchronized.

* Store **preprocessor.pkl**, **scaler.pkl**, and **model.pkl** — DVC tracks all of them.

* Use separate directories:

  * `data/raw/`
  * `data/processed/`
  * `data/features/`
  * `final_model/`

* Add `params.yaml` for hyperparameters.

* Integrate DVC stages with CI/CD (GitHub Actions).

---

## 7. Summary: Key things you must be able to explain

* What DVC does: **data versioning, pipeline orchestration, model storage**
* Why DVC: Git cannot handle large datasets; DVC solves reproducibility
* How to install & initialize DVC
* How to add data & model artifacts (with `.dvc` files)
* How to set up remote (S3 is common)
* How to define pipelines in `dvc.yaml`
* How to run experiments (`dvc exp`)
* How DVC fits into the entire MLOps workflow
* How it supports deployment (model → Docker → ECR → EC2)

---

If you want, I can also create **one combined README** covering **MLflow + DVC + CI/CD + AWS Deployment**—very powerful in interviews.
