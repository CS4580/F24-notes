## Setting Up Your Development Environment

### Task 1: Creating a New Virtual Environment

1. **Objective**: 
   - The goal of this task is to ensure that you can create and manage a virtual environment using `Conda`, which will help maintain a clean and consistent development environment for your projects.

2. **Instructions**:

   - **Step 1: Open Your Terminal or Anaconda Prompt**
     - On Windows, you can use the Anaconda Prompt or Command Prompt.
     - On macOS/Linux, open your terminal.

   - **Step 2: Create a New Virtual Environment**
     - Use the following command to create a new virtual environment. Replace `env_name` with a name of your choice (e.g., `data_science_env`):
       ```bash
       conda create --name env_name python=3.12
       ```
     - Press `Y` when prompted to confirm the installation of packages.

   - **Step 3: Activate the Virtual Environment**
     - Once the environment is created, activate it using the following command:
       ```bash
       conda activate env_name
       # or 
       activate env_name
       ```

   - **Step 4: Verify the Environment**
     - To verify that your environment is active and running the correct version of Python, type:
       ```bash
       python --version
       ```
     - You should see something like `Python 3.10.x`, depending on the version you specified.

### Task 2: Installing Required Packages

1. **Objective**:
   - This task will guide you through installing the necessary Python packages for this assignment using a `requirements.txt` file.

2. **Instructions**:

   - **Step 1: Ensure Your Environment is Activated**
     - Make sure your virtual environment is active. If not, activate it using:
       ```bash
       conda activate env_name
       # or 
       activate env_name
       ```

   - **Step 2: Locate the `requirements.txt` File**
     - The `requirements.txt` file should be provided in the assignment materials. It lists all the packages needed for this assignment.

   - **Step 3: Install the Packages**
     - Run the following command to install the packages listed in `requirements.txt`:
       ```bash
       # Using Conda
       conda install --file requirements.txt
       
       # or using pip
       pip install -r requirements.txt
       ```
     - This command will automatically install all the required packages into your virtual environment.

   - **Step 4: Verify the Installation**
     - After installation, you can verify that the packages were installed correctly by running:
       ```bash
       conda list
       ```
     - Ensure that the packages listed in `requirements.txt` appear in the output.

Other references:https://bobbyhadz.com/blog/conda-create-and-install-requirements-txt 

### Submission Checklist

Before you proceed with the rest of the assignment, ensure that you have:

- [ ] Created and activated a new Conda virtual environment.
- [ ] Installed all required packages using `requirements.txt`.
- [ ] Verified that your environment is set up correctly.

---