import os
import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Set the scope and API key file path
SCOPES = ['https://www.googleapis.com/auth/admin.directory.group.member.readonly',
          'https://www.googleapis.com/auth/admin.directory.group.readonly']
SERVICE_ACCOUNT_FILE = 'deimos-groups-optimization-e257e793dba3.json'

def main():
    """This is a basic usage of the Admin SDK Group API.
    Exports all groups and members of the group into an Excel Workbook. Each group is exported to a sheet on the workbook. 
    """
    # Authenticate and create the service object
    creds = None
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('admin', 'directory_v1', credentials=creds)

    # Retrieve all the groups in the domain
    groups = service.groups().list(domain='deimos.co.za').execute()

    # Initialize an empty list to store the members of each group
    all_members = []

    # Loop through each group and retrieve its members
    for group in groups['groups']:
        members = service.members().list(groupKey=group['email']).execute()
        # If the group has no members, skip it
        if 'members' not in members:
            continue
        # Create a DataFrame to store the members of this group
        group_members_df = pd.DataFrame(columns=['Group', 'Member Email'])
        for member in members['members']:
            if 'email' not in member:
                continue
            group_members_df = group_members_df.append(
                {'Group': group['name'], 'Member Email': member['email']}, 
                ignore_index=True)
        # Append the group's members to the list of all members
        all_members.append(group_members_df)

    # Concatenate all the group members DataFrames into one
    all_members_df = pd.concat(all_members)

    # Write the DataFrame to an Excel file
    writer = pd.ExcelWriter('group_members.xlsx')
    for group in groups['groups']:
        group_name = group['name']
        group_df = all_members_df[all_members_df['Group'] == group_name]
        group_df.to_excel(writer, sheet_name=group_name, index=False)
    writer.save()

if __name__ == '__main__':
    main()