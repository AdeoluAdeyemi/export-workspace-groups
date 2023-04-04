# export-workspace-groups

This is a basic usage of the Admin SDK Group API.
The groups_export.py script will exports all groups and members of the group into an Excel Workbook. Each group is exported to a sheet on the workbook.

## Prequisite

### Step 1: Create a project

1. Go to [Google Cloud](https://console.developers.google.com/) and sign in as a super administrator. If it's your first time signing in to the console, agree to the Terms of Service.
2. Click IAM & Adminand thenManage Resources. You might have to click Menu "" first.
3. At the top, click Create Project and enter a project name.
4. (Optional) To add the project to a folder, for Location, click Browse, navigate to the folder, and click Select.
5. Click Create.
6. By default, only the creator of the project has rights to manage the project. To ensure the project can be maintained if the creator leaves the organization, you should assign at least one other person the role of Project Owner. For details, go to Manage access to projects, folders, and organizations.

### Step 2: Turn on the APIs for the service account

1. Check the box next to your new project.
2. Click APIs & Servicesand thenLibrary. You might have to click Menu "" first.
3. For each API you require (below), click the API name and then Enable:
4. Admin SDK

'''
    Tip: If you can't find the API, specify the API name in the search box.

### Step 3: Set up the OAuth consent screen

'''
    Tip: When adding the email addresses below, use shared administrator email accounts.

1. Click APIs & Servicesand thenOAuth consent screen. You might have to click Menu "" first.
2. For User Type, select Internal.
3. Click Create.
4. For App name, add the name of your application. 
5. Select a User support email for users to contact with questions.
6. For Developer contact information, enter email addresses so Google can contact you about changes to your project.
7. Click Save and Continueand thenSave and Continueand thenBack to Dashboard.

### Step 4: Create the service account

1. Click APIs & Servicesand thenCredentials. You might have to click Menu "" first.
2. Click Create Credentialsand thenService account.
3. For Service account name, enter a name for the service account.
4. (Optional) For Service account description, enter a description of the service account.
5. Click Create and Continue.
6. Click Doneand thenSave.
7. At the top, click Keysand thenAdd Keyand thenCreate new key.
8. Make sure the key type is set to JSON and click Create.
9. You'll get a message that the service account's private key JSON file was downloaded to your computer. Make a note of the file name and where your browser saves it. You'll need it later.
10. Click Close.

### Step 5: Add the service account as a Group Admin

To grant a service account access to the Groups API, you can use the "Groups Administrator" role or the "Group Owner" role. These roles provide sufficient permissions to manage Google Workspace groups and their members.

Here are the steps to grant a service account access to the Groups API using the "Groups Administrator" role:

1. Go to the [Google Workspace Admin console](https://admin.google.com/) and sign in as a super administrator.
2. Click on "Roles" in the left sidebar.
3. Search for "Groups Administrator" and select it.
4. Click on "Add Another" in the "Members" section and enter the email address of the service account that you created.
5. Click "Save" to grant the "Groups Administrator" role to the service account.

## Usage

1. Set the SERVICE_ACCOUNT_FILE name to the name of the downloaded JSON file.
2. Run the script groups.export.py
3. View the exported groups in the .xlsx file
