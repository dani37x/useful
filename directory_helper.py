import os



def segregation(path='path/to/your/folder/'):
  important_files = ['']
  for file in os.listdir(path):
    if file not in important_files and file != 'templates' and not file.endswith('_files'):
      end_file = file.split('.')
      start_file = end_file[0]
      end_file = end_file[1]
      directory = '{}_{}'.format( start_file, end_file)
      if directory in os.listdir():
        os.system('mv ' + start_file+'.'+end_file +' ' +end_file+'_files')
      else:
        os.system('mkdir ' + end_file +'_files')
        os.system('mv ' + start_file+'.'+end_file +' ' +end_file+'_files') 
