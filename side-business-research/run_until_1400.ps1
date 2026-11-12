\xEF\xBB\xBF# 14:00までAI副業リサーチのサイクルを回す
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
Set-Location $PSScriptRoot
New-Item -ItemType Directory -Force -Path "cycles" | Out-Null

$deadline = (Get-Date).Date.AddHours(14)
$i = (Get-ChildItem "cycles" -Filter "cycle_*.md" -ErrorAction SilentlyContinue).Count + 1

while ((Get-Date) -lt $deadline) {
    $left = [int]($deadline - (Get-Date)).TotalMinutes
    Write-Host "===== サイクル $i 開始（14:00まで残り $left 分）=====" -ForegroundColor Cyan

    $prompt = "サイクル $i を実行してください。CLAUDE.md の手順に従い、サブエージェントを使って cycles/cycle_$i.md を作成し、report.md を更新したら終了してください。"

    claude -p $prompt `
        --allowedTools "Read,Write,Edit,Glob,WebSearch,WebFetch,Task" `
        --max-turns 60 2>&1 | Tee-Object -FilePath "cycles/log_$i.txt"

    $i++
    Start-Sleep -Seconds 20
}
Write-Host "14:00になったので終了しました。結論は report.md を見てください。" -ForegroundColor Green
