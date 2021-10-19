$url = $args[0]
Write-Output $url
conda activate pic16b
Set-Location .\IMDB_scraper\
try {
    Remove-Item movies.csv
}
catch {
    Write-Output "movies.csv ain't here boss"
}
if($null -ne $url)
{
    scrapy crawl imdb_spider -o movies.csv -a url=$url
}else{
scrapy crawl imdb_spider -o movies.csv 
}
Set-Location ..
Write-Output "analysis time"
python analysis.py