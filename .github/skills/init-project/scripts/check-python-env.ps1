param(
    [switch]$AsJson
)

$result = [ordered]@{
    environmentType = 'none'
    environmentName = $null
    pythonCommand = $null
    pythonVersion = $null
    isActiveEnvironment = $false
    isSupportedVersion = $false
    isReady = $false
    reason = $null
}

if ($env:CONDA_DEFAULT_ENV) {
    $result.environmentType = 'conda'
    $result.environmentName = $env:CONDA_DEFAULT_ENV
    $result.isActiveEnvironment = $true
} elseif ($env:VIRTUAL_ENV) {
    $result.environmentType = 'venv'
    $result.environmentName = Split-Path -Leaf $env:VIRTUAL_ENV
    $result.isActiveEnvironment = $true
}

$pythonCommand = $null
if (Get-Command python -ErrorAction SilentlyContinue) {
    $pythonCommand = 'python'
} elseif (Get-Command py -ErrorAction SilentlyContinue) {
    $pythonCommand = 'py'
}

$result.pythonCommand = $pythonCommand

if ($pythonCommand) {
    try {
        $rawVersion = if ($pythonCommand -eq 'py') {
            & py -c "import sys; print('.'.join(map(str, sys.version_info[:3])))"
        } else {
            & python -c "import sys; print('.'.join(map(str, sys.version_info[:3])))"
        }

        if ($LASTEXITCODE -eq 0 -and $rawVersion) {
            $result.pythonVersion = $rawVersion.Trim()
            $version = [Version]$result.pythonVersion
            $result.isSupportedVersion = $version -ge [Version]'3.12.0'
        }
    } catch {
        $result.reason = $_.Exception.Message
    }
}

if (-not $result.isActiveEnvironment) {
    $result.reason = 'No hay un entorno conda o venv activo.'
} elseif (-not $result.pythonVersion) {
    $result.reason = 'No se pudo determinar la version de Python del entorno activo.'
} elseif (-not $result.isSupportedVersion) {
    $result.reason = "La version de Python activa es $($result.pythonVersion) y se requiere 3.12 o superior."
} else {
    $result.isReady = $true
    $result.reason = 'Entorno Python valido.'
}

if ($AsJson -or $true) {
    $result | ConvertTo-Json -Depth 3
} else {
    $result
}