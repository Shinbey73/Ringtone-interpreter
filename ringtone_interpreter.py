
#########IMPORT STATEMENTS##########

#add all your import statements here
import unittest
#############UNITTEST###############

class RingtoneTestCase(unittest.TestCase):

    def test1(self):
        """
        This will test the correctness of input in check_valid_note function.
        There are valid and invalid input.

        Input:
            1) Some of the invalid input will have more than one invalid characteristic.
            2) Characteristics of the input are length, pitch and scale of the note.
            3) If a full stop (.) is found anywhere other than at the end of the input, the condition will be considered false."
        """
        #valid example
        self.assertTrue(check_valid_note("1a3"), "Invalid length")
        self.assertTrue(check_valid_note("8c#2"), "Invalid pitch")
        self.assertTrue(check_valid_note("16g5."), "Invalid scale")

        # #invalid example
        self.assertFalse(check_valid_note('32l.'), "Invalid pitch")
        self.assertFalse(check_valid_note(''), "Cannot be an empty string")
        self.assertFalse(check_valid_note("p#m"), "Invalid pitch and scale")
        self.assertFalse(check_valid_note("5b14"), "Invalid length and scale" )
        self.assertFalse(check_valid_note("10f#"), "Invalid length and pitch")
        self.assertFalse(check_valid_note('13m11'), "Invalid length, scale and pitch")
        self.assertFalse(check_valid_note(".1a3"), "wrong placement of the fullstop, fullstop should be at the end of the input")
        self.assertFalse(check_valid_note("1.a3"), "wrong placement of the fullstop, fullstop should be at the end of the input")

    def test2(self):
        """
        This will test the correctness of input in generate_valid_ringtone function.
        There are valid and invalid input.

        Input:
            1) Some of the input will have more than one characterisitc of invalid input.
            2) Characteristics of of the input are title, default value and note data.
         """

        self.assertFalse(generate_valid_ringtone('d=3-o=9-b80:32p-4c#-8  c#-2g-8G-8A#-8A#-    G'), 'The default values declarations are incomplete, missing proper commas and a  note pitch. Output: []')
        self.assertFalse(generate_valid_ringtone('Dance baby: d=4,b=80,o=5:16p,2c,2c,2g,8G,8A,8A,G, c=80:32p,8c,8c,8g,8G,8A,8A,G'), 'unacceptable declaration and incorrect declaration order. Output: []')
        self.assertFalse(generate_valid_ringtone(' d=41,o=2,b=80:32p,8c,8c,40g,8g,30a,8a,12g6'), 'Not acceptable note length and unacceptable note length. Output: []')
        self.assertTrue(generate_valid_ringtone('  coco n u  t Song : d=4,o =6, b= 120:8  a,8 b,8c'), "unnecessary whitespace" )
        self.assertTrue(generate_valid_ringtone(':d=2,o=7,b=80:16a,16b,16c'), "invalid default value and note data")
        self.assertTrue(generate_valid_ringtone('8  a,8 b,8c'), "invalid note date")

    def test3(self):
        """
        This test will check whether the type returned is the correct type.
        There are valid and invalid inputs

        """
        self.assertTrue(isinstance(check_valid_note("8g3"), bool) , "Invalid type. Expected type: boolean)")
        self.assertTrue(isinstance(generate_valid_ringtone('ocotpus :d=1,o=2,b=34:4c,4d#,8c#,g'), list) , 'Invalid type. Expected type: list')
        self.assertFalse(isinstance(check_valid_note("5b14"), list), 'Invalid type. Expected type: boolean' )
        self.assertFalse(isinstance(generate_valid_ringtone('Triple Kid:d=4, b=80, o=5:16a,16b,16c#,12g6'), str), 'Invalid type. Expected type: list')

    def test4(self):
        """
        Test cases for white spaces whether at the beginning, in the middle or the end of the input of the generate_valid_ringtone function
        will make the function return an empty string, [].
        """

        self.assertTrue(generate_valid_ringtone('  Peter  pant : d =4 ,o=5, b=8 0:16a,2g,  8a , 4a#,g  '), 'White spaces in the input. Output: []')
        self.assertTrue(generate_valid_ringtone('   d =8   ,o =6  ,b =1 20:16 a,16 b,16 c  '), 'White spaces in the title. Output: []')
        self.assertTrue(generate_valid_ringtone('   Ring    the bell: d=1,  o= 2, b =3: 8e   , 8e   , 8e,  8 e, 8e, 8e, 8e, 8e, 8e, 8e, 8e, 8e   '), 'White spaces in default values. Output: []')

###############TASK 1###############

def check_valid_note(note):
    """
Verifies the validity of a musical note.

Parameters:
- note (str): The musical note to be checked for validity.

Returns:
- bool: True if the note is valid, False otherwise.
    """

    # Valid note lengths, pitches, and scales
    valid_lengths = {'1', '2', '4', '8','16', '32',''}
    valid_pitches = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'p', 'a#', 'b#', 'c#', 'd#', 'e#', 'f#', 'g#'}
    valid_scales = {'1', '2', '3', '4', '5', '6', '7', '8',''}
    full_stop = {'.',''}


    list = []
# Generates every possible valid note
    for length in (valid_lengths):
        for pitch in (valid_pitches):
            for scale in (valid_scales):
                for stop in (full_stop):
                    # concatenates all lengths pitches and scales by order
                    Note = (f"{length}{pitch}{scale}{stop}")

                    list.append(Note)
# Check if the provided note is in the list of valid notes
    if note in list:
        return True

    else:
        return False

###############TASK 2###############

def generate_valid_ringtone(string):
    """
Creates a valid ringtone data structure based on the input string.

Parameters:
- string (str): Input string containing ringtone details.

Returns:
- list: A list comprising the title, default values, and note data for a valid ringtone; returns an empty list if the input is invalid.
    """

    delimiter = ':'
    splitted = string.split(delimiter)

    #default values to store each list of data
    note_data_list = ''
    default_value_list = ''
    title_list = ''
    
    #checks if list of splitted string contains 3 values and assigns to value based on index 
    if len(splitted) == 3:
        temp_note_data = splitted[2]
        temp_default_data = splitted[1]
        temp_title = splitted[0]
        
        #checks whether each note is valid
        if check_valid_note(temp_note_data):
            note_data_list = splitted[-1]
            title_list = string.split(':')[0]
            
            # checks whether default values are valid
            if check_default_values(temp_default_data):
                formatted_note_data = temp_note_data.replace(' ', '').lower()
                note_val = formatted_note_data.split(',')
                note_data_list = formatting(note_val)
                default_value_list = check_default_values(temp_default_data)
            else:
                return [] #returns empty list if not valid values
        else:
            return [] #returns empty list if not valid notes

    #checks if list splitted string contains 2 values and assigns to value
    elif len(splitted) == 2:
        temp_note_data = splitted[1]

        if check_valid_note(temp_note_data):
            formatted_note_data = temp_note_data.replace(' ', '').lower() #removes any additional spaces
            note_val = formatted_note_data.split(',') #uses comma as delimiter to split note values

            temp_default_data = splitted[0]
            note_data_list = formatting(note_val)

            if check_default_values(temp_default_data):
                default_value_list = check_default_values(temp_default_data)
            else:
                return []
        else:
            return []

    elif len(splitted) == 1:
        temp_note_data = splitted[0]
        if check_valid_note(temp_note_data):
            formatted_note_data = temp_note_data.replace(' ', '').lower() #removes any additional spaces
            note_val = formatted_note_data.split(',') #uses comma as delimiter to split note values
            note_data_list = formatting(note_val)
        else:
            return []
    else:
        return []

    return [format_title(title_list), default_value_list, note_data_list]

###############TASK 4###############

def get_ringtone_notes(default_values, note_data):
    """
Transforms song note data and default values into a list of lists, each containing note duration and playback numbers.

Parameters:
- default_values (str): Default values for the song formatted as "d=x, o=x, b=x".
- note_data (str): Note data for the song, with each note separated by commas.

Returns:
- result (list): A list of lists, each representing note duration and playback numbers for an individual note.
    """
    #Define default values if not provided
    if default_values == "":
        default_values = 'd=4,o=5,b=60'
    duration, octave , beat = get_default_values(default_values)

    # Step 1: Split the <note data> string into individual notes
    notes = note_data.replace(' ', '').split(',')

    # Initialize an empty list to store the note data
    note_list_length = []
    note_list_pitch = []
    note_list_scale = []
    note_list_fullstop = []
    note_list = []

    # Step 2: For each note, split it into the note length, note pitch, and full stop
    for note in notes:
        if '.' in note:
            note = note.replace('.', '')
            full_stop = 'True'
            p = note.split(',')
            if len(p[0]) > 3:
                if p[0][0].isdigit():
                    if p[0][1].isdigit():
                        if p[0][-1].isdigit():
                            nl = str(p[0][0]) + str(p[0][1])
                            np = str(p[0][2])
                            if p[0][3] == '#':
                                np = str(p[0][2]) + str(p[0][3])
                                ns = str(p[0][-1])
                            else:
                                np = str(p[0][2])
                                ns = str(p[0][3])
                        else:
                            nl = str(p[0][0]) + str(p[0][1])
                            np = str(p[0][2])
                            if p[0][3] == '#':
                                np = str(p[0][2]) + str(p[0][3])
                                ns = octave
                            else:
                                np = str(p[0][2])
                                ns = octave

                    else:
                        nl = str(p[0][0])
                        np = str(p[0][1])
                        ns = str(p[0][-1])
                        if str(p[0][2]) == '#':
                            np = str(p[0][1]) + str(p[0][2])
                        else:
                            np = str(p[0][1])

            elif len(p[0])>2:
                if p[0][0].isdigit():
                    if p[0][1].isdigit():
                        nl = str(p[0][0]) + str(p[0][1])
                        np = str(p[0][2])
                        ns = octave
                    else:
                        nl = str(p[0][0])
                        np = str(p[0][1])
                        if str(p[0][2]) == '#':
                            np = str(p[0][1]) + str(p[0][2])
                            ns = octave
                        else:
                            ns = str(p[0][2])

            elif len(p[0])>1:
                if p[0][0].isdigit():
                    nl = str(p[0][0])
                    ns = octave
                    np = str(p[0][1])

                else:
                    np = str(p[0][0])
                    nl = duration
                    if str(p[0][1]) == '#':
                        np = str(p[0][0]) + str(p[0][1])
                        ns = octave
                    else:
                        ns = str(p[0][1])
            else:
                np = str(p[0][0])
                nl = duration
                ns = octave

        else:
            full_stop = 'False'
            p = note.split(',')
            if len(p[0]) > 3:
                if p[0][0].isdigit():
                    if p[0][1].isdigit():
                        if p[0][-1].isdigit():
                            nl = str(p[0][0]) + str(p[0][1])
                            np = str(p[0][2])
                            if p[0][3] == '#':
                                np = str(p[0][2]) + str(p[0][3])
                                ns = str(p[0][-1])
                            else:
                                np = str(p[0][2])
                                ns = str(p[0][3])
                        else:
                            nl = str(p[0][0]) + str(p[0][1])
                            np = str(p[0][2])
                            if p[0][3] == '#':
                                np = str(p[0][2]) + str(p[0][3])
                                ns = octave
                            else:
                                np = str(p[0][2])
                                ns = octave

                    else:
                        nl = str(p[0][0])
                        np = str(p[0][1])
                        ns = str(p[0][-1])
                        if str(p[0][2]) == '#':
                            np = str(p[0][1]) + str(p[0][2])
                        else:
                            np = str(p[0][1])

            elif len(p[0])>2:
                if p[0][0].isdigit():
                    if p[0][1].isdigit():
                        nl = str(p[0][0]) + str(p[0][1])
                        np = str(p[0][2])
                        ns = octave
                    else:
                        nl = str(p[0][0])
                        np = str(p[0][1])
                        if str(p[0][2]) == '#':
                            np = str(p[0][1]) + str(p[0][2])
                            ns = octave
                        else:
                            ns = str(p[0][2])
                else:
                    nl = duration
                    if str(p[0][1]) == '#':
                        np = str(p[0][0]) + str(p[0][1])
                        ns = str(p[0][-1])

            elif len(p[0])>1:
                if p[0][0].isdigit():
                    nl = str(p[0][0])
                    ns = octave
                    np = str(p[0][1])

                else:
                    np = str(p[0][0])
                    nl = duration
                    if str(p[0][1]) == '#':
                        np = str(p[0][0]) + str(p[0][1])
                        ns = octave
                    else:
                        ns = str(p[0][1])

            else:
                np = str(p[-1])
                nl = duration
                ns = octave

        note_list_length.append(nl)
        note_list_pitch.append(np)
        note_list_scale.append(ns)
        note_list_fullstop.append(full_stop)

        # Calculate total duration using the provided function
        total_duration = calculating_note_duration(note_list_length, note_list_fullstop, beat)

        # Get playback numbers using the provided function
        playback_numbers = get_playback_note_numbers(note_list_pitch, note_list_scale)

        # Combine duration and playback_numbers into a list of lists
        result = [list(note) for note in zip(total_duration, playback_numbers)]
    return result

###############TASK 5###############

def generate_commands(ringtone_note, song_title):
    """
Create JavaScript commands and play buttons based on the provided ringtone notes and song titles.

Arguments:
- ringtone_note (list): List of ringtone note data for each valid song.
- song_title (list): List of titles for each valid song.

Returns:
- final_function_string (str): Concatenated JavaScript functions for playing each song.
- final_play_button (str): Concatenated HTML play buttons for each song.
    """

    final_function_string = ''
    final_play_button = ''
    command = ''
    play_button = ''
    # seperates each list of titles and ringtones into respective values
    for i in range (len(ringtone_note)):
        song_notes = ringtone_note[i]
        title = song_title[i]

        if title == '':
            title = "UNTITLED SONG"

        else:
            title = title.upper()
        # if there is more than 1 value then splits the string by line
        if i > 0:
            command = "\n"
            play_button = "\n"

        command += f"function play{i}() "

        command += "{\n"

        current_time = 0.0

        # seperates song_notes into duration and playback based on index
        for j in range (len(song_notes)):
            note_duration = song_notes[j][0]
            note_playback = song_notes[j][1]

            rounded_time = round(current_time, 2)

            if rounded_time.is_integer():
                rounded_time = f"{rounded_time:.1f}" # adds 1 decimal point to rounded time if time is integer
            else:
                rounded_time = str(rounded_time)

            command += f"var audioBufferSourceNode = player.queueWaveTable(AC, AC.destination, preset, AC.currentTime+{rounded_time}, {note_playback}, {note_duration});\n"

            current_time += note_duration # increments total time based on each note duration 

        command +="}"

        final_function_string += command

        play_button += f"<p><a href='javascript:play{i}();'>PLAY {title}</a></p>"

        final_play_button += play_button

    return final_function_string, final_play_button

###############TASK 6###############
"""
Converts a text file containing song data into an HTML file with play buttons for each valid song.

Parameters:
- text_file (str): The path to the input text file.

Returns:
- all_title (list): A list of titles for valid songs.
- all_ringtones (list): A list of corresponding ringtone data for valid songs.

"""
def convert_song_file(text_file):
    # Open the text file in read mode
    new_file = open(text_file,'r')
    print (f"Read {len(new_file.readlines())} lines from \"{text_file}\".")

    # Read all lines from the file and remove trailing whitespaces
    every_song = [line.rstrip() for line in open(text_file,'r')]

    count = 0

    all_title = []
    all_ringtones = []

    # Iterate through each song in the file
    for song in every_song:
         # Check if the song is a valid ringtone
         if generate_valid_ringtone(song) != []:
            # Get the valid ringtone data
            valid_ringtone = generate_valid_ringtone(song)
            count += 1

            # Extract title, duration, octave, and beat from the valid ringtone and append the extracted information to respective lists
            all_title.append(valid_ringtone[0])
            all_ringtones.append(get_ringtone_notes(valid_ringtone[1], valid_ringtone[2]))

    print (f"Generated {count} valid songs.")
    
    # Generate commands and play buttons for the HTML file
    commands, play_button = generate_commands(all_ringtones, all_title)
    # # Generate and write HTML content to a new file
    generate_html(commands, play_button)

    return all_title, all_ringtones

#####ADDITIONAL HELPER FUNCTIONS#####
#add all your additional helper functions here

# Extract default values from the string
def get_default_values(default_str):
    # Define default values
    default_duration = '4'
    default_octave = '5'
    default_beat = '60'
    parameter = {}
    for item in default_str.split(','):
        key, value = item.split('=')
        parameter[key] = value

    duration = str(parameter.get('d', default_duration))
    octave = str(parameter.get('o', default_octave))
    beat = str(parameter.get('b', default_beat))
    return duration, octave, beat
# Extract note duration from the string
def calculating_note_duration(note_list_length, note_list_fullstop, beat):
    nl_value = {'1': 4, '2': 2, '4': 1,
                '8': 0.5, '16': 0.25, '32': 0.125,
                'False': 1, 'True': 1.5}

    total_duration = []
    beat = int(beat)
    for note_length, full_stop in zip(note_list_length, note_list_fullstop):
        if note_length in nl_value:
            fs_value = nl_value[full_stop]
            note_duration = round((nl_value[note_length] * (60 / beat)) * fs_value, 2)
            total_duration.append(note_duration)


    return total_duration
#Extract playback number from the string
def get_playback_note_numbers(note_list_pitch, note_list_scale):
    note_scale_map = {
        'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5, 'F#': 6, 'G': 7, 'G#': 8, 'A': 9, 'A#': 10, 'B': 11,
        'P': -400
    }

    octave_range = {
        '1': [0, 12],
        '2': [12, 24],
        '3': [24, 36],
        '4': [36, 48],
        '5': [48, 60],
        '6': [60, 72],
        '7': [72, 84],
        '8': [84, 96]
    }

    playback_numbers = []

    combined_list = [f"{pitch}{scale}" for pitch, scale in zip(note_list_pitch, note_list_scale)]
    result_list = [element.upper() for element in combined_list[:-1]]
    result_list.append(combined_list[-1].upper())

    for i in result_list:
        if 'P' in i:
            playback_numbers.append(-400)
        else:
            pitch_value = note_scale_map[i[:-1]]  # Remove the last character (the scale)
            octave_range_value = octave_range.get(i[-1], [0, 0])  # Take the last character (the scale) for octave range
            playback_numbers.append(pitch_value + octave_range_value[0])

    return playback_numbers

#Define a function to check if a given note data is valid
def check_valid_note(note_data):
        # Valid note lengths, pitches, and scales
        valid_lengths = {'1', '2', '4', '8', '16', '32', ''}
        valid_pitches = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'p', 'a#', 'b#', 'c#', 'd#', 'e#', 'f#', 'g#'}
        valid_scales = {'1', '2', '3', '4', '5', '6', '7', '8', ''}
        full_stop = {'.', ''}

        delimiter1 = ','
        list= []

        formatted_note_data = note_data.replace(' ', '').lower()
        note_val = formatted_note_data.split(delimiter1)

        for length in valid_lengths:
            for pitch in valid_pitches:
                for scale in valid_scales:
                    for stop in full_stop:
                        Note = f"{length}{pitch}{scale}{stop}"
                        list.append(Note)

        valid_note = ''
        valid = True
        for notes in (note_val):
            if notes not in list:
                valid = False
                break
        return valid

# Define a function to check if the default values are valid
def check_default_values(temp_default_data):
    delimiter1 = ','
    formatted_default_value = temp_default_data.replace(' ', '').lower()
    values = formatted_default_value.split(delimiter1)

    def check_positive(integer):
        integer = integer.split('=')[-1]
        if int(integer) > 0:
            return True
        else:
            return False

    if len(values) == 3:
        if 'd=' in values[0] and check_positive(values[0]):
            if 'o=' in values[1] and check_positive(values[1]):
                if 'b=' in values[2] and check_positive(values[2]):
                    return formatting(values)

# Define a function to format the default values
def formatting(value_list):
    all_values = ''
    for value in value_list:
        all_values += value
        all_values += ','
    all_values = all_values[:-1]
    return all_values

# Define a function to format the title
def format_title(title):
    p = title.strip()
    return p

def generate_html(commands, play_button):
    html = f"""<html>
                       <head>
                       <script src='WebAudioFontPlayer.js'></script>
                       <script src='Soundfile_sf2.js'></script>
                       <script>
                       var preset=soundfile_sf2;
                       var AudioContextFunc = window.AudioContext || window.webkitAudioContext;
                       var AC = new AudioContextFunc();
                       var player=new WebAudioFontPlayer();
                       player.adjustPreset(AC,preset);
                       {commands}
                       </script>
                       </head>
                       <body>
                       <h1>"Mamba Number Py" Ringtone Interpreter🎵</h1>
                       {play_button}
                       </body>
                       </html>"""

    with open("play_ringtones.html", "w") as song_html:
        song_html.write(html)
#############MAIN FUNCTION###########

def run():
    """
The Main function for executing the Ringtone Interpreter.
Reads a song file, processes it, provides options to discard and modify songs, and creates an HTML file.
    """

    print("------------------------------------------")
    print("\"Mamba Number Py\" Ringtone Interpreter🎵")
    print("------------------------------------------")

    #Asking for file to read
    file_path = input("\nFile to read? ")  

    # Read,process the file and unpack the song_title and ringtone_note
    song_title, ringtone_note = convert_song_file(file_path)

    if not ringtone_note or not song_title:
        print("Error processing file. Exiting.")
        return

    #print out the list of songs
    print("\n---------------SONG TITLES----------------")
    i = 0
    for title in song_title:
        print(f"{i}  {title}")
        i += 1
    print("------------------------------------------")

    #discard the song
    discard_songs = input("\nSelect songs to discard (e.g., 1,2,4 or NONE): ")
    if discard_songs.upper() == 'NONE': # if it is none, no song will discard
        new_song_title = song_title
        new_ringtone_note = ringtone_note

    else: #else, we will discard the song the want to be discarded with the song's ringtone
        discard_list = list(map(int, discard_songs.split(',')))
        new_song_title = []
        new_ringtone_note = []

        for i in range(len(song_title)):
            if i not in discard_list:
                new_song_title.append(song_title[i])
                new_ringtone_note.append(ringtone_note[i])

    #print out the list of songs that not being discraded
    print("\n---------------SONG TITLES----------------")
    i = 0
    for title in new_song_title:
        print(f"{i}  {title}")
        i += 1
    print("------------------------------------------")

    while True:
        #asking any song to be modified
        modify_songs = input("\nDo you wish to modify any songs (Y/N)? ").upper()
        # if no, it will go out form the loop
        if modify_songs != 'Y':
            break
        #print out the list of songs that not being discraded
        print("\n---------------SONG TITLES----------------")
        i = 0
        for title in new_song_title:
            print(f"{i}  {title}")
            i += 1
        print("------------------------------------------")
        
        #asking which song to modify
        modify_song_index = int(input("\nSelect song to modify: "))

        if 0 <= modify_song_index < len(new_ringtone_note):
            #print out the option for the song to be modified
            print("\n1 - Double length of each note (slower)")
            print("2 - Half length of each note (faster)")
            print("3 - Increase octave of each note")
            print("4 - Decrease octave of each note")
            #asking the option that user want to choose
            modification_option = input("\nSelect option: ")
            # Ensure the input is a valid integer
            while not modification_option.isdigit() or int(modification_option) not in [1, 2, 3, 4]:
                print("Invalid input. Please enter a valid option (1, 2, 3, or 4).")
                modification_option = input("\nSelect option: ")

            modification_option = int(modification_option)

            if modification_option in [1]:
                # Adjust note length
                adjusted_ringtone = adjust_note_length(new_ringtone_note, modify_song_index, modification_option)
                print(f'{new_song_title[modify_song_index]} now plays 2 times slower.')
                #ringtone_note = adjusted_ringtone

            elif modification_option in [2]:
                # Adjust note length
                adjusted_ringtone = adjust_note_length(new_ringtone_note, modify_song_index, modification_option)
                print(f'{new_song_title[modify_song_index]} now plays 2 times faster.')
                #ringtone_note = adjusted_ringtone

            elif modification_option in [3]:
                # Adjust note scale (octave)
                octave_adjustment = int(input("How many octaves do you wish to increase? "))
                adjusted_ringtone = adjust_note_scale_positive(new_ringtone_note, song_title, modify_song_index, octave_adjustment)
                print(f'{new_song_title[modify_song_index]} now {octave_adjustment} octave higher.')

            else:
                # Adjust note scale (octave)
                octave_adjustment = int(input("How many octaves do you wish to decrease? "))
                adjusted_ringtone = adjust_note_scale_negative(new_ringtone_note, song_title, modify_song_index, octave_adjustment)
                print(f'{new_song_title[modify_song_index]} now {octave_adjustment} octave lower.')

        else:
            print("Invalid song index. Please select a valid index.")
    
    #unpack the final_function_string and final_play_button fun generate_commands function
    final_function_string, final_play_button = generate_commands(new_ringtone_note, new_song_title)
    #generate the html
    generate_html(final_function_string, final_play_button)

    print("\n\play_ringtone.html\ file is generated and ready to play!")
    
    #ask the users either they want to run unittest on Task 3 before exiting or not
    run_unittest = input("\nDo you wish to run unittest on Task 3 before exiting (Y/N)? ").upper()
    #run the unittest
    if run_unittest == 'Y':
        unittest.main()

def adjust_note_scale_positive(new_ringtone_note, new_song_title, title_index, octave_adjustment):
    """ 
    Adjusts the note scale (octave) for a certain tune.

    Parameters:
    - new_ringtone_note (list): a list of songs containing notes.
    - new_song_title (list): a list of song titles.
    - title_index (int): The song index that has to be modified.
    - octave_adjustment (int): The number of octaves to be increased.

    Returns:
    - a list of adjusted ringtones for the provided music.
    """

    adjusted_ringtone = new_ringtone_note[title_index].copy()
    for note in adjusted_ringtone:
        # Adjust the note scale by the specified octave_adjustment
        if note[1] != -400:
            note[1] += (octave_adjustment*12)

    return adjusted_ringtone

def adjust_note_scale_negative(new_ringtone_note, new_song_title, title_index, octave_adjustment):
    """ 
    Adjusts the note scale (octave) for a certain tune.

    Parameters:
    - new_ringtone_note (list): a list of songs containing notes.
    - new_song_title (list): a list of song titles.
    - title_index (int): The song index that has to be modified.
    - octave_adjustment (int): The number of octaves to reduce.

    Returns a list of adjusted ringtones for the provided music.
    """

    adjusted_ringtone = new_ringtone_note[title_index].copy()
    
    for note in adjusted_ringtone:
        # Adjust the note scale by the specified octave_adjustment
        if note[1] != -400:
            note[1] -= (octave_adjustment*12)
    return adjusted_ringtone

def adjust_note_length(new_ringtone_note, title_index, option):
    """ 
    Changes the note length of a specific song.

    Parameters:
    - new_ringtone_note (list): A list of songs and their respective notes.
    - title_index (int): The index of the song to be updated.
    - option (int): Option to change note length (1 for double, 2 for half).

    Returns: 
    - list: Updated list of notes for the given song. 
    """
    #change the note length either go faster or slower
    adjusted_ringtone = new_ringtone_note[title_index].copy()
    for note in adjusted_ringtone:
        # Double note length
        if option == 1:
            note[0] *= 2
        # Half note length
        elif option == 2:
            note[0] /= 2
    return adjusted_ringtone

if __name__ == "__main__":
    run()
