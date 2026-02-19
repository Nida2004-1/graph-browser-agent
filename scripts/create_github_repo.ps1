Param(
    [string]$RepoName = "",
    [ValidateSet("public","private")]
    [string]$Visibility = "public"
)

function Abort($msg) { Write-Host $msg -ForegroundColor Red; exit 1 }

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Abort "git not found. Please install Git and run this script again."
}

$hasGh = $false
if (Get-Command gh -ErrorAction SilentlyContinue) { $hasGh = $true }

if (-not $RepoName) { $RepoName = Read-Host "Enter GitHub repo name (e.g. pcl_agent)" }
if (-not $RepoName) { Abort "Repo name required." }

Write-Host "Initializing git repository..."
git init
git add -A
git commit -m "chore: initial commit for $RepoName" || Write-Host "No changes to commit or commit failed." -ForegroundColor Yellow

if ($hasGh) {
    Write-Host "Creating GitHub repo and pushing (using gh)..."
    if ($Visibility -eq 'public') {
        gh repo create $RepoName --public --source=. --remote=origin --push --confirm
    } else {
        gh repo create $RepoName --private --source=. --remote=origin --push --confirm
    }
    Write-Host "Repository created and pushed." -ForegroundColor Green
} else {
    Write-Host "gh CLI not found. Create a repository on GitHub and run the commands below:" -ForegroundColor Yellow
    Write-Host "git branch -M main"
    Write-Host "git remote add origin https://github.com/<your-username>/$RepoName.git"
    Write-Host "git push -u origin main"
}
