import os
import os
import argparse
import textwrap


class Prog:
    def __init__(self, args):
        htmlTemplate = """<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" href="style.css">
</head>"""
        path = os.path.join(os.getcwd(), args.dir)
        os.mkdir(path)
        # os.chdir(path)
        with open(os.path.join(path, 'index.html'), 'w') as index:
            index.write(htmlTemplate)
        with open(os.path.join(path, 'script.js'), 'w') as script:
            script.write("// script.js ")
        with open(os.path.join(path, 'style.css'), 'w') as style:
            style.write("// style.css")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='*** Javascript Template Project Creator Tool ***',
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog=textwrap.dedent('''- Example: prog.py -d Desktop/DefaultJSProject'''))
    parser.add_argument('-d', '--dir', default='Desktop/DefaultJSProject',
                        help='Specified project folder path.')
    args = parser.parse_args()
    prog = Prog(args)

    #currentDir = os.getcwd().__str__
    # os.mkdir(self.args[1])

# def chooseDir(self):
