def unzip(filename, path):
    # Get dir of zipfile
    zipfile = os.path.join(path, filename)
    path = os.path.dirname(zipfile)

    # Create a ZipFile Object
    with ZipFile(zipfile, 'r') as zip_obj:
        # Get a list of all archived file names from the zip
        list_files = []
        list_files = zip_obj.namelist()

        # Iterate over the file names
        for file in list_files:
            name, ext = os.path.splitext(file)
            zip_obj.extract(file, os.path.dirname(zipfile))
            os.rename(os.path.join(path, file), os.path.join(path, os.path.splitext(filename)[0]+ext))
            print('File "{}" extracted as "{}" in "{}" directory.'.format(file, os.path.splitext(filename)[0]+ext, path))

    # Remove file
    #os.remove(zipfile)
    
def get_download(url, filename, path):
    # Define o nome do arquivo, com diretório, que será salvo
    zipfile = os.path.join(path, filename)

    # Faz o download do arquivo da 'url' e salva localmente com o nome do arquivo
    r = requests.get(url, stream=True)
    with open(zipfile, 'wb') as out:
        for chunk in r.iter_content(chunk_size=128):
            out.write(chunk)
    
    print(f'File "{filename}" download in "{path}" directory.')
    
    
# Deleta Shapefile
file = 'sp_defesacivil'
shp = os.path.join('data', 'shps', '{}.shp'.format(file))
driver = ogr.GetDriverByName('ESRI Shapefile')

# Delete shapefile
if os.path.exists(shp):
    driver.DeleteDataSource(shp)

# Delete other files
for i in os.listdir(os.path.dirname(shp)):
    if i.split('.')[0] == file:
        os.remove(os.path.join('data', 'shps', i))