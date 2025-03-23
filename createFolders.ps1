<#
.SYNOPSIS
    Creates a folder structure with a parent folder and a specified number of subfolders.

.DESCRIPTION
    This script allows you to create a parent folder (if it does not exist) and a specified number of subfolders with a given naming prefix.

.PARAMETER parentFolder
    The path where the parent folder will be created.

.PARAMETER subFolderPrefix
    The naming prefix for each subfolder.

.PARAMETER numberOfSubFolders
    The total number of subfolders to create under the parent folder.

.EXAMPLE
    .\createFolders.ps1 -parentFolder "C:\Projects" -subFolderPrefix "SubProject" -numberOfSubFolders 5
    
    Creates a parent folder `C:\Projects` with 5 subfolders named `SubProject 1` through `SubProject 5`.

.NOTES
    Author: Algenis A. Romero
    Version: 1.0
    Date: 27 February 2025

#>

param (
    [ValidateNotNullOrEmpty()]
    [string]$parentFolder,

    [ValidateNotNullOrEmpty()]
    [string]$subFolderPrefix,

    [ValidateRange(1, [int]::MaxValue)]
    [int]$numberOfSubFolders,

    [switch]$Help
)


# Display help information if the -Help parameter is used
if ($Help) {
    Get-Help $MyInvocation.MyCommand.Path
    exit
}

try {
    # Create the parent folder if it does not exist
    if (-not (Test-Path -Path $parentFolder)) {
        New-Item -ItemType Directory -Path $parentFolder
    }

    # Create the subfolders
    for ($i = 1; $i -le $numberOfSubFolders; $i++) {
        $subFolderName = "$parentFolder\$subFolderPrefix $i"
        New-Item -ItemType Directory -Path $subFolderName
    }
    Write-Host "Folder structure created successfully!"
}catch{
    Write-Host "An error occurred while creating the folder structure, type -Help for more information."
}