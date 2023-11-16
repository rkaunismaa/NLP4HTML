1) ScrapeNewMatchAccounts.py - reads from the latest MatchProfilesMasterList and creates NewUsers.
2) ScrapeMatch_FromUserList.py - reads from NewUsers and creates NewProfiles and FailedProfiles
3) ReScanFailedProfiles2NewProfiles.py - reads from FailedProfiles and creates to UpdatedNewProfiles 
4) AppendNewProfiles2MySql.py - reads from UpdatedNewProfiles and appends these records into MySql
5) DownloadMatchImages.py - reads from UpdatedNewProfiles and pulls down all images into the matchImages folder
6) CreateProfileMaster.py - reads from the current MatchProfilesMasterList and UpdatedNewProfiles and creates the newest MatchProfilesMasterList