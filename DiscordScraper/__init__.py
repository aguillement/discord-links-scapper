"""                                                                                                      ""
""                                   Discord Scraper/Archiver Script                                     ""
""                                   ===============================                                     ""
""                                                                                                       ""
""                          A script written specifically for the ease of archiving                      ""
""                              Discord guild contents for long-term reference                           ""
""                                                                                                       ""
""                                       Main Package Initializer                                        ""
""                                                                                                      """

# Who is the creator of this package
__author__ = 'Dracovian'

# BSD Zero-Clause (0BSD) license to replace the previous WTF Public License (WTFPL)
__license__ = '0BSD'

# A copyright is needed for 0BSD even though I refute the necessity of a copyright for this project
__copyright__ = 'Copyright 2022 Dracovian'

# We're still working within an alpha release, it's stable enough to be used but with bugs and issues
__version__ = '1.0a'

# Set the directories for this package
__path__ = __import__('pkgutil').extend_path(__path__, __name__)

# Create an empty class for the purpose of converting dictionary items into class objects
class Objectifier(object):
    pass
