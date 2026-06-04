param(
    [string]$EnvironmentPath = '.venv'
)

function Get-Python312Command {
    if (Get-Command py -ErrorAction SilentlyContinue) {
        & py -3.12 -c "import sys; print('.'.join(map(str, sys.version_info[:3])))" *> $null
        if ($LASTEXITCODE -eq 0) {
            return @('py', '-3.12')
        }
    }

    if (Get-Command python -ErrorAction SilentlyContinue) {
        $version = & python -c "import sys; print('.'.join(map(str, sys.version_info[:3])))"
        if ($LASTEXITCODE -eq 0 -and ([Version]$version.Trim()) -ge [Version]'3.12.0') {
            return @('python')
        }
    }

    if (Get-Command python3 -ErrorAction SilentlyContinue) {
        $version = & python3 -c "import sys; print('.'.join(map(str, sys.version_info[:3])))"
        if ($LASTEXITCODE -eq 0 -and ([Version]$version.Trim()) -ge [Version]'3.12.0') {
            return @('python3')
        }
    }

    return $null
}

$pythonCommand = Get-Python312Command
if (-not $pythonCommand) {
    throw 'No se encontro un interprete Python 3.12 o superior para crear el entorno virtual.'
}

if (Test-Path $EnvironmentPath) {
    throw "La ruta '$EnvironmentPath' ya existe."
}

if ($pythonCommand.Count -eq 2) {
    & $pythonCommand[0] $pythonCommand[1] -m venv $EnvironmentPath
} else {
    & $pythonCommand[0] -m venv $EnvironmentPath
}

if ($LASTEXITCODE -ne 0 -or -not (Test-Path (Join-Path $EnvironmentPath 'Scripts\python.exe'))) {
    throw 'No se pudo crear el entorno virtual.'
}

[ordered]@{
    environmentPath = (Resolve-Path $EnvironmentPath).Path
    activationCommand = ".\$EnvironmentPath\Scripts\Activate.ps1"
    pythonCommandUsed = ($pythonCommand -join ' ')
    status = 'created'
} | ConvertTo-Json -Depth 3