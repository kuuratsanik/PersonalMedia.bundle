import datetime, os, time

# Only use unicode if it's supported, which it is on Windows and OS X,
# but not Linux. This allows things to work with non-ASCII characters
# without having to go through a bunch of work to ensure the Linux 
# filesystem is UTF-8 "clean".
#
def unicodize(s):
  filename = s
  if os.path.supports_unicode_filenames:
    try: filename = unicode(s.decode('utf-8'))
    except: pass
  return filename

def Start():
  pass
  
class PlexPersonalMediaAgentMovies(Agent.Movies):
  name = 'Personal Media'
  languages = [Locale.Language.NoLanguage]
  
  def search(self, results, media, lang):
    
    # Compute the GUID based on the media hash.
    part = media.items[0].parts[0]
    
    # Get the modification time to use as the year.
    filename = unicodize(part.file)
    mod_time = os.path.getmtime(filename)
    
    results.Append(MetadataSearchResult(id=part.hash, name=media.name, year=time.localtime(mod_time)[0], lang=lang, score=100))
      
  def update(self, metadata, media, lang):
    
    # Get the filename and the mod time.
    filename = unicodize(media.items[0].parts[0].file)
    mod_time = os.path.getmtime(filename)
    
    date = datetime.date.fromtimestamp(mod_time)
    
    # Fill in the little we can get from a file.
    try: title = os.path.splitext(os.path.basename(filename))[0]
    except: title = media.title
      
    metadata.title = title
    metadata.year = date.year
    metadata.originally_available_at = Datetime.ParseDate(str(date)).date()
    
class PlexPersonalMediaAgentTVShows(Agent.TV_Shows):
  name = 'Personal Media Shows'
  languages = [Locale.Language.NoLanguage]

  def search(self, results, media, lang):
    results.Append(MetadataSearchResult(id=media.id, name=media.show, year=None, lang=lang, score=100))

  def update(self, metadata, media, lang):
    metadata.title = media.title

class PlexPersonalMediaAgentArtists(Agent.Artist):
  name = 'Personal Media Artists'
  languages = [Locale.Language.NoLanguage]

  def search(self, results, media, lang):
    results.Append(MetadataSearchResult(id=media.id, name=media.artist, year=None, lang=lang, score=100))

  def update(self, metadata, media, lang):
    metadata.title = media.title

class PlexPersonalMediaAgentAlbums(Agent.Album):
  name = 'Personal Media Albums'
  languages = [Locale.Language.NoLanguage]

  def search(self, results, media, lang):
    results.Append(MetadataSearchResult(id=media.id, name=media.album, year=None, lang=lang, score=100))

  def update(self, metadata, media, lang):
    metadata.title = media.title
    
class PlexPersonalMediaAgentPhotos(Agent.Photos):
  name = 'Photos'
  languages = [Locale.Language.NoLanguage]

  def search(self, results, media, lang):
    results.Append(MetadataSearchResult(id=media.id, name=media.title, year=None, lang=lang, score=100))

  def update(self, metadata, media, lang):
    metadata.title = media.title
