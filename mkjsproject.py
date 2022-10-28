import os
import argparse
import textwrap

from os.path import exists


class Prog:
    def __init__(self, args):
        htmlTemplate = """<!-- index.html-->
<html lang="en">
    <head>
         <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" type="text/css" href="style.css">
    </head>
    <body>
        
        <script type="text/javascript" src="main.js"></script>
    </body>
</html>
        """
        settingsFile = '.settings.txt'
        workspace = ''

        if (exists(os.path.join(os.getcwd(), settingsFile))):
            with open(os.path.join(os.getcwd(), settingsFile), 'r') as settings:
                workspace = settings.readline()
                settings.close()
        else:
            workspace = input('''To begin, provide the absolute path to your desired workspace folder.
This will act as the default folder that all projects will be saved to once set: 
''')
            workspace = workspace + '/'
            with open(os.path.join(os.getcwd(), settingsFile), 'w') as settings:
                settings.write("{}".format(workspace))

        if (args.default):
            workspace = args.default
            workspace = workspace + '/'
            with open(os.path.join(os.getcwd(), settingsFile), 'w') as settings:
                settings.write("{}".format(workspace))
                settings.close()

        if (args.save):
            projectFilePath = os.path.join(workspace, args.save)
            os.mkdir(os.path.join(workspace, args.save))
            newProjectFolder = os.path.join(workspace, args.save)
            with open(os.path.join(newProjectFolder, 'index.html'), 'w') as index:
                index.write(htmlTemplate)
            with open(os.path.join(newProjectFolder, 'main.js'), 'w') as script:
                script.write("// main.js ")
            with open(os.path.join(newProjectFolder, 'style.css'), 'w') as style:
                style.write("/* style.css */")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='*** Javascript Template Project Creator Tool ***',
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog=textwrap.dedent('''ARGUMENTS:
    New Project:        -s || --save
    Change workspace:   -d || --default

USAGE: 
    New Project:            mkjsproject -s newProjectName
    Change workspace:       mkjsproject -d /Users/<your_user_name>/Desktop'''))
    parser.add_argument(
        '-s', '--save', help='Create a new project.')
    parser.add_argument(
        '-d', '--default', help='Change default workspace where projects are saved.')
    args = parser.parse_args()
    prog = Prog(args)
