import datetime, os, time

def Start():
  pass
  
class PlexMovieAgent(Agent.Movies):
  name = 'Home Movies'
  languages = [Locale.Language.English, Locale.Language.Swedish, Locale.Language.French, 
               Locale.Language.Spanish, Locale.Language.Dutch, Locale.Language.German, 
               Locale.Language.Italian]
  
  def search(self, results, media, lang):
    
    # Compute the GUID based on the media hash.
    part = media.items[0].parts[0]
    
    # Get the modification time to use as the year.
    filename = part.file.decode('utf-8')
    mod_time = os.path.getmtime(filename)
    
    results.Append(MetadataSearchResult(id=part.plexHash, name=media.name, year=time.localtime(mod_time)[0], lang=lang, score=100))
      
  def update(self, metadata, media, lang):
    
    # Get the filename and the mod time.
    filename = media.items[0].parts[0].file.decode('utf-8')
    mod_time = os.path.getmtime(filename)
    
    date = datetime.date.fromtimestamp(mod_time)
    
    # Fill in the little we can get from a file.
    metadata.title = media.title
    metadata.year = date.year
    metadata.originally_available_at = Datetime.ParseDate(str(date)).date()
    