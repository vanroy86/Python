""" Copyright (C) 2015  IrrelevantPenguin

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA."""
    
import os, fnmatch, optparse

class Makefile(object):
    def __init__(self, path):
        self.path = path
        self.find_all_dir()

    def find_all_dir(self):
        self.file_list = []
        for self.top_dir in os.listdir(self.path): # Find all top level directories and ignore files
            if os.path.isfile(self.top_dir):
                pass
            else:
                for self.sub_dir in os.listdir(self.path + self.top_dir): # Find all files in sub directories
                    k = self.path + self.top_dir +  "/" + self.sub_dir
                    print k
                    if fnmatch.fnmatch(k, "*.c"): # If the file type is C source code then skip it
                        pass
                    else:
                        self.file_list.append(k)
        return self.file_list

    def add_c_flags(self, cflags): # Add CFLAGS to the top of file
        file_to_open = self.path + "Makefile"
        with open(file_to_open, "w") as make_file:
             make_file.write(cflags + "\n\n")

    def create_make_file(self, section_header, section_body):
        file_to_open = self.path + "Makefile"
        with open(file_to_open, "a") as make_file:
             make_file.write(section_header)
             for i in self.file_list:
                 clean_section = section_body + i + "\n"
                 make_file.write(clean_section)

def main():
    parser = optparse.OptionParser("Usage: -p <Target Path> -f <Specify CFLAGS>")
    parser.add_option("-p", dest = "path", type = "string", help = "Specify a Target Path")
    parser.add_option("-f", dest = "cflags", type = "string", help = "Specify CFLAGS")

    (options, args) = parser.parse_args()

    if (options.path == None):
        print parser.usage
        exit(0)
    else:
        path = options.path
        cflags = options.cflags

    if os.path.exists(path + "Makefile"):
        os.remove(path + "Makefile")

    make_file_creator = Makefile(path)
    make_file_creator.add_c_flags(cflags)
    section_header = "clean:\n"
    section_body = "\trm -f "
    make_file_creator.create_make_file(section_header, section_body)
    section_header = "all:\n"
    section_body = "\tmake "
    make_file_creator.create_make_file(section_header, section_body)

if __name__ == "__main__":
    main()
