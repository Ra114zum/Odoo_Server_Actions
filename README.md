# Odoo_Server_Actions
Odoo Server Actions for Various Data Clean_Up and Redundant Tasks

# **Odoo BOM Cleanup Tools**  

**Automated Server Actions for Cleaning Bill of Materials (BOM) in Odoo**  

This repository contains Python scripts for Odoo server actions that help maintain clean and efficient Bill of Materials (BOM) by:  

- **Removing archived products** from BOM lines  
- **Detecting and removing duplicate products** in BOM components  
- **Combined cleanup action** for both archived and duplicate products  

## **Features**  

✔ **Easy Integration** – Works as an Odoo server action  
✔ **Studio-Compatible** – Can be implemented via Odoo Studio with minimal setup  
✔ **Multi-BOM Support** – Processes single or multiple BOMs at once  
✔ **User Notifications** – Provides clear feedback on cleanup results  
✔ **Efficient ORM Queries** – Optimized for performance  

## **Usage**  

1. **Remove Archived Products**  
   - Searches for BOM lines containing archived products and removes them.  

2. **Remove Duplicate Products**  
   - Detects multiple entries of the same product in a BOM and keeps only one.  

3. **Combined Cleanup (Archived + Duplicates)**  
   - Performs both actions in a single run for maximum efficiency.  

## **Implementation**  

- **Via Odoo Studio**:  
  - Create server actions and paste the provided Python code.  
  - Add buttons to BOM views for easy access.  

- **Manual XML Installation**:  
  - Deploy via custom module for better control.  

## **Why Use This?**  

✅ **Prevents Errors** – Ensures BOMs only contain active, non-duplicate components  
✅ **Improves Performance** – Clean BOMs load faster and avoid confusion  
✅ **Maintenance-Friendly** – Runs on demand or can be scheduled  

---  
**Powered by Hsx TECH** 🚀  

*(Need customization? Contact Hsx TECH for Odoo solutions!)*  

---  

### **Repository Structure**  
```
📂 odoo-bom-cleanup/  
├── README.md  
├── remove_archived_products.py  
├── remove_duplicate_products.py  
└── combined_cleanup_action.py  
```  

### **License**  
MIT License – Free to use and modify.  

---  
**Contribute or Report Issues**  
Feel free to fork, improve, or suggest enhancements!  


**Powered by Hsx TECH** – *Collaborate, Lead, Innovate* 
