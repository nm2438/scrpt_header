########################################################################################
#======================================================================================#
#||                               _       _                    _                     ||#
#||           ___  ___ _ __ _ __ | |_    | |__   ___  __ _  __| | ___ _ __           ||#
#||          / __|/ __| '__| '_ \| __|   | '_ \ / _ \/ _` |/ _` |/ _ \ '__|          ||#
#||          \__ \ (__| |  | |_) | |_    | | | |  __/ (_| | (_| |  __/ |             ||#
#||          |___/\___|_|  | .__/ \__|___|_| |_|\___|\__,_|\__,_|\___|_|             ||#
#||                        |_|      |_____|                                          ||#
#||                                                                                  ||#
#======================================================================================#
#||                                   scrpt_header                                   ||#
#||                                       v0.1                                       ||#
#======================================================================================#
#||                                                                                  ||#
#||                           Written by: Nicholas Morris                            ||#
#||                        Contact: https://github.com/nm2438                        ||#
#||                                                                                  ||#
#||                                 Date: 13AUG2020                                  ||#
#||                                                                                  ||#
#======================================================================================#
#||    Generates a nice-looking header for your scripts                              ||#
#======================================================================================#
########################################################################################


import pyfiglet


def print_line(frmt, wdth, lines):
    '''
    Description:
        Prints the arguments in a pre-set manner
    Args:
        frmt - str
        wdth - int
        lines - list
    Returns:
        None
    '''
    [print(frmt.format(item, wdth)) for item in lines]


def listerator(text, wdth):
    '''
    Description:
        Breaks up a long string into a list of strings that fit
        nicely into a box of the given width
    Args:
        text - str
        wdth - width
    Returns:
        list of strings
    '''
    word_lst = list(text.split())
    word_lst.reverse()

    lines = ['']
    ctr = 0
    for _ in range(len(word_lst)):
        if len(lines[ctr]) + len(word_lst[-1]) + 1 > wdth:
            ctr += 1
            lines.append('')
        new_word = word_lst.pop()
        if not len(lines[ctr]) == 0:
            new_word = ' ' + new_word
        lines[ctr] += new_word

    return lines


def print_block(text, width, line, pad):
    '''
    Description:
        Formats a very long string into a nice block of text
    Args:
        text - str - a string to be printed
        width - int - the width of the 'box' to print in
        line - str - the string representation of the upper/lower box border
        pad - int - number of spaces between box border and text block
    Returns:
        None
    '''
    # generate box dimensions, formats
    txt_wdth = width-(2*pad)-4
    #num_lines = (len(text)//txt_wdth)+1
    frmt = '#||{1}{0}{1}||#'.format('{0:<{1}}', ' '*pad)

    # print block
    print(line)
    print_line(frmt, txt_wdth,
               listerator(text, txt_wdth))
    print(line)


def print_header(script_name, version_no, author, contact, date, description, titlepad=24):
    '''
    Description:
        Pieces together the various printing functions
    Args:
    Returns:
        None
    '''
    # generate pretty title
    title = pyfiglet.figlet_format(script_name)
    title_lst = title.split('\n')

    # generate box dimensions, formats
    width = max([len(line) for line in title_lst]) + titlepad
    inner_width = width - 4
    line = '{0}{1}{0}'.format('#', '='*width)
    outer_line = '#'*(width+2)
    frmt = '#||{0:^{1}}||#'

    # print the pretty title
    print(outer_line, line, sep='\n')
    [print(frmt.format(''.join(line), inner_width)) for line in title_lst]

    # print out the middle box
    print(line)
    print_line(frmt, inner_width,
               [script_name, 'v' + version_no])
    print(line)
    print_line(frmt, inner_width,
               ['', 'Written by: ' + author, 'Contact: ' + contact, '', 'Date: ' + date, ''])

    # print the description
    print_block(description, width, line, 4)
    print(outer_line)


if __name__ == '__main__':
    # edit header text
    script_name = 'scrpt_header'
    version_no = '0.1'
    author = 'Nicholas Morris'
    contact = 'https://github.com/nm2438'
    date = '13AUG2020'
    description = 'Generates a nice-looking header for your scripts'

    # call printing function
    print_header(script_name, version_no, author, contact, date, description)
