# music_crawler

Web page crawler for crawling information of popular singers / songs / albums / singer-song pairs

## Currently supporting:

1. KKBOX
2. myMusic
3. Spotify
4. qqmusic


## Structure:

multi_crawler() -> main_crawler() -> language_crawler() -> individual_crawler_module() 

*multi_crawler():* run a multithread process for crawling info in different languages  
*main_crawler():* main wrapper for language_crawler() with the data concatention function  
*language_crawler():* wrapper function for multiple dates input for the basic crawler  
*individual_crawler_module():* customized fundamental crawler for different webpage   

## How to run:

Pick / write a customized fundamental crawler and call:

1. multi_crawler(): for faster crawling  
2. main_crawler(): for data concatention  

### Data is already downloaded. If you need the raw data, feel free to contact the author.
