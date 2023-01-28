import os

# specify the directory where the articles are located
directory = 'path/to/articles'

# loop through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.md'):
        # open the file and read its contents
        with open(os.path.join(directory, filename), 'r') as f:
            file_contents = f.read()

        # extract the tags from the file contents (assuming they are listed on a line starting with "Tags: ")
        tags = []
        for line in file_contents.split('\n'):
            if line.startswith('Tags: '):
                tags = line.split(': ')[1].split(', ')
                break
        
        # if the file doesn't have any tags, create them
        if not tags:
            tags = ["tag1", "tag2", "tag3"]
            # write the tags to the file
            with open(os.path.join(directory, filename), 'w') as f:
                f.write(file_contents + '\nTags: ' + ', '.join(tags))
                print(f'Tags: {tags} added to {filename}')
        else:
            print(f'Tags already exists in {filename}')

