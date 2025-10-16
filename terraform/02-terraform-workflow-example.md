# Workflow Example: Default Terraform Development Workflow

---

## Introduction

This document illustrates a **default Terraform workflow** for infrastructure projects.
It guides developers on how to **organize, manage, and safely apply** Terraform code.

---

## 1. Setup

### Initialize a new Terraform project

```bash
terraform init
```

* Downloads provider plugins.
* Prepares the working directory for Terraform commands.

### Check Terraform version

```bash
terraform --version
```

---

## 2. Plan Your Infrastructure

Before applying changes, always preview them:

```bash
terraform plan -out=tfplan
```

* `-out=tfplan` saves the plan to a file.
* Shows what Terraform will create, modify, or destroy.

---

## 3. Apply Changes

Apply the infrastructure changes safely:

```bash
terraform apply tfplan
```

* Executes the plan created in the previous step.
* Always review the plan before applying.

---

## 4. Make Configuration Changes

1. **Edit Terraform files** (`.tf`) in your editor.
2. **Validate syntax and configuration**:

```bash
terraform validate
```

3. **Format files**:

```bash
terraform fmt
```

---

## 5. Update Infrastructure

After changes, repeat plan and apply:

```bash
terraform plan -out=tfplan
terraform apply tfplan
```

* Ensures changes are predictable and safe.

---

## 6. Manage State (Optional but Important)

### List resources in state

```bash
terraform state list
```

### Show details of a resource

```bash
terraform state show {resource_name}
```

### Remove resource from state without destroying it

```bash
terraform state rm {resource_name}
```

---

## 7. Destroy Infrastructure

Clean up all resources when no longer needed:

```bash
terraform destroy
```

* Always review the destroy plan before executing.

---

## 8. Undo Mistakes (Optional)

### Unlock state if blocked

```bash
terraform force-unlock {LOCK_ID}
```

* Useful if a previous apply failed or was interrupted.

---

## Summary Workflow Diagram

```text
init → validate → fmt → plan → apply → edit → plan → apply → state management → destroy
```

---

## Notes

* Keep **Terraform configurations modular** (use modules for reuse).
* Always **review plans before applying** to avoid accidental changes.
* Use **remote state** for collaboration or backup.
* Follow naming conventions for **resources and variables** for clarity.
