'''
Created on Dec 21, 2019

@author: colinbitterfield

Global Variables to be used by different classes
'''

video_list = ['codec_name', 'codec_long_name', 'codec_type', 'width', 'height', 'coded_width', 'coded_height', 
              'display_aspect_ratio', 'avg_frame_rate', 'bit_rate', 'disposition', 'tags']

audio_list = ['codec_name', 'codec_long_name', 'codec_type', 'sample_rate', 'channels', 'avg_frame_rate', 
              'bit_rate', 'max_bit_rate', 'disposition', 'tags']

format_list = ['filename', 'nb_streams', 'nb_programs', 'format_name', 'format_long_name', 'start_time', 
                'duration', 'size', 'bit_rate', 'probe_score', 'tags']


tags_list = ['major_brand', 'minor_version', 'compatible_brands', 'creation_time', 'date', 'make', 'title', 
             'synopsis', 'episode_id', 'network', 'episode_sort', 'show', 'purchase_date', 'description', 
             'genre', 'season_number', 'media_type', 'iTunEXTC', 'track', 'album', 'album_artist', 'artist', 
             'iTunMOVI']

image_list = ['colorspace','compression','compression_quality','depth','format','height','mimetype','orientation','page_height','page_width','type','width']

image_meta_list = ['date:create', 'date:modify', 'exif:ApertureValue', 'exif:BrightnessValue', 'exif:ColorSpace', 
              'exif:ComponentsConfiguration', 'exif:DateTime', 'exif:DateTimeDigitized', 'exif:DateTimeOriginal', 
              'exif:DigitalZoomRatio', 'exif:ExifImageLength', 'exif:ExifImageWidth', 'exif:ExifOffset', 'exif:ExifVersion', 
              'exif:ExposureBiasValue', 'exif:ExposureMode', 'exif:ExposureProgram', 'exif:ExposureTime', 'exif:Flash', 
              'exif:FlashPixVersion', 'exif:FNumber', 'exif:FocalLength', 'exif:FocalLengthIn35mmFilm', 'exif:ISOSpeedRatings', 
              'exif:Make', 'exif:MakerNote', 'exif:MeteringMode', 'exif:Model', 'exif:Orientation', 'exif:ResolutionUnit', 
              'exif:SceneCaptureType', 'exif:SceneType', 'exif:SensingMethod', 'exif:ShutterSpeedValue', 'exif:Software', 
              'exif:SubjectArea', 'exif:SubSecTimeDigitized', 'exif:SubSecTimeOriginal', 'exif:thumbnail:Compression', 
              'exif:thumbnail:JPEGInterchangeFormat', 'exif:thumbnail:JPEGInterchangeFormatLength', 'exif:thumbnail:ResolutionUnit', 
              'exif:thumbnail:XResolution', 'exif:thumbnail:YResolution', 'exif:WhiteBalance', 'exif:XResolution', 
              'exif:YCbCrPositioning', 'exif:YResolution', 'icc:copyright', 'icc:description', 'icc:manufacturer', 
              'icc:model', 'jpeg:colorspace', 'jpeg:sampling-factor']

mp4_meta_list    = ['title']


pdf_meta_list = ['Author',
             'CreationDate',
             'Creator',
             'Keywords',
             'ModDate',
             'Producer',
             'Subject',
             'Title']

doc_meta_list = ['Author']

xls_meta_list = []



# Lists for types of images
EXTENSIONS_PIL = ['jpg', 'jpeg', 'jpe', 'png', 'bmp', 'gif', 'pcd', 'tif', 'tiff', 'j2k', 'j2p', 'j2x', 'webp','cr2']
EXTENSIONS_PIL_EXTRA = ['eps', 'ico', 'im', 'pcx', 'ppm', 'sgi', 'spider', 'xbm', 'tga']
EXTENSIONS_MAGICK = ['psd', 'xcf']
EXTENSIONS_PDF = ['pdf']
EXTENSIONS_VIDEO = ['avi', 'mp4', 'mov', 'mpeg', 'mpg', 'm2p', 'mkv', '3gp', 'ogg', 'flv', 'f4v', 'f4p', 'f4a', 'f4b']
EXTENSIONS_AUDIO = ['mp3', 'mp2']
EXTENSIONS_DOCS = ['txt','rtf','doc','docx','xls','xlsx','csv']

EXTENSIONS_IMAGE = EXTENSIONS_PIL + EXTENSIONS_PIL_EXTRA + EXTENSIONS_MAGICK
EXTENSIONS_DOCUMENT = EXTENSIONS_DOCS + EXTENSIONS_PDF


sql_tables = dict()
sql_tables['image'] = dict({
    'file_name'     : 'text',
    'file_size'     : 'text',
    'file_magic'    : 'text',
    'file_md5'      : 'text',
    'file_type'     : 'text', 
    'file_valid'    : 'text',  
    'file_basename' : 'text',
    'file_dirname'  : 'text'  
    })

sql_tables['video'] = dict({
    'file_name'     : 'text',
    'file_size'     : 'text',
    'file_magic'    : 'text',
    'file_md5'      : 'text',
    'file_type'     : 'text', 
    'file_valid'    : 'text',  
    'file_basename' : 'text',
    'file_dirname'  : 'text'      
    })

sql_tables['error'] = dict({
    'file_name'     : 'text',
    'file_size'     : 'text',
    'file_magic'    : 'text',
    'file_md5'      : 'text',
    'file_type'     : 'text', 
    'file_valid'    : 'text',  
    'file_basename' : 'text',
    'file_dirname'  : 'text',
    'file_error'    : 'text'
    })

sql_tables['document'] = dict({
    'file_name'     : 'text',
    'file_size'     : 'text',
    'file_magic'    : 'text',
    'file_md5'      : 'text',
    'file_type'     : 'text', 
    'file_valid'    : 'text',  
    'file_basename' : 'text',
    'file_dirname'  : 'text'      
    })

sql_tables['other'] = dict({
    'file_name'     : 'text',
    'file_size'     : 'text',
    'file_magic'    : 'text',
    'file_md5'      : 'text',
    'file_type'     : 'text', 
    'file_valid'    : 'text',  
    'file_basename' : 'text',
    'file_dirname'  : 'text'      
    })


# Extend the sql_tables from lists
for column_name in image_list:
    sql_tables['image'].update({'image_' + column_name : 'text'})
    
for column_name in image_meta_list:
    sql_tables['image'].update({'meta_' + column_name : 'text'})
    
for column_name in video_list:
    sql_tables['video'].update({'video_' + column_name : 'text'})
    
for column_name in audio_list:
    sql_tables['video'].update({'audio_' + column_name : 'text'})
    
for column_name in mp4_meta_list:
    sql_tables['video'].update({'meta_' + column_name : 'text'})

    
for column_name in format_list:
    sql_tables['video'].update({'format_' + column_name : 'text'})
    
for column_name in format_list:
    sql_tables['video'].update({'tags_' + column_name : 'text'})

for column_name in pdf_meta_list:
    sql_tables['document'].update({'pdf_' + column_name : 'text'})
    
for column_name in doc_meta_list:
    sql_tables['document'].update({'doc_' + column_name : 'text'})
    
for column_name in xls_meta_list:
    sql_tables['document'].update({'xls_' + column_name : 'text'})



