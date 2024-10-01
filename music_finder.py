from apis import spotify
from apis import sendgrid
import time

selected_genres_output=['none selected']
selected_artists_output=['none selected']
selected_artist_ids=[]
def print_menu():
    global selected_genres_output
    print('''
---------------------------------------------------------------------
Settings / Browse Options

Instructions: Select up to 5 filters (genres and artists) to generate
a list of song recommendations from Spotify!
---------------------------------------------------------------------
''', '\n1 - Select your favorite genres', selected_genres_output,

'\n2 - Select your favorite artists', selected_artists_output,
'\n3 - Discover new music ',         
'\n4 - Quit',
'''\n
---------------------------------------------------------------------
    ''')

def handle_genre_selection():
    '''
    OBJECTIVES:
    1. Allow user to select one or more genres using the 
        spotify.get_genres_abridged() function
    2. Allow user to store / modify / retrieve genres
        in order to get song recommendations 
    '''
    global selected_genres_output
    available_genres= spotify.get_genres_abridged()
    counter=1
    template = '{counter:>10}{genres:<15}'
    for genre in available_genres:
        print(
            template.format(counter=str(counter)+'. [ ] ',genres=genre)
        )
        counter+=1

    while True:
        try:
            selected_genres=input('Please select up to three genres as a comma-delimited list of numbers. Type "clear" to clear your selections:')
            if selected_genres=='clear':
                selected_genres_output=['none selected']
                break
            selected_genres=selected_genres.split(',')
            #print(selected_genres)

            if selected_genres_output==['none selected']:
                selected_genres_output.pop()

            for genre in selected_genres:
                if int(genre) in range(counter):
                    selected_genres_output.append(available_genres[int(genre)-1])
                else:
                    print('Next time, please input a number/list of numbers that corresponds with a genre/set of genres in the list above.')
                    selected_genres_output=['none selected']
            break

        except:
            print('Next time, please input a number/list of numbers that corresponds with a genre/set of genres in the list above.')
            continue


def handle_artist_selection():
    '''
    OBJECTIVES:
    1. Allow user to search for an artist using 
       spotify.get_artists() function
    2. Allow user to store / modify / retrieve artists
       in order to get song recommendations 
    '''
    global selected_artists_output
    global selected_artist_ids
    search_term=input('Enter the name of an artist:')
    found_artists=spotify.get_artists(search_term)
    #print(found_artists)
    artist_counter=1
    template2 = '{artist_counter:>10}{name:<25}'
    for artist in found_artists:
        print(
            template2.format(artist_counter=str(artist_counter)+'. ',name=artist.get('name'))
        )
        artist_counter+=1
    while True:
        try:
            selected_artists=input('Please select up to three artists as a comma-delimited list of numbers or type "clear" to clear your selections:')
            if selected_artists=='clear':
                selected_artists_output=['none selected']
                selected_artist_ids=[]
                break
            selected_artists=selected_artists.split(',')

            if selected_artists_output==['none selected']:
                selected_artists_output.pop()

            for artist in selected_artists:
                #print(artist)
                if int(artist) in range(artist_counter):
                    selected_artists_output.append(found_artists[int(artist)-1].get('name'))
                    selected_artist_ids.append(found_artists[int(artist)-1].get('id'))
                    #print(selected_artist_ids)
                else:
                    print('Please input a number/list of numbers, corresponding to up to three artists in the list above.')
                    selected_artists_output=['none selected']
                    selected_artist_ids=[]
            break

        except:
            print('Please input a number/list of numbers, corresponding to up to three artists in the list above.')
            continue

def get_recommendations():
    '''
    OBJECTIVES:
    1. Allow user to retrieve song recommendations using the
        spotify.get_similar_tracks() function
    2. List them below
    3. In addition to showing the user recommendations, allow them
        to email recommendations to one or more of their friends using
        the sendgrid.send_mail() function.
    '''
    
    try:
        if selected_artist_ids and selected_genres_output != ['none selected']:
            recommendations=spotify.get_similar_tracks(artist_ids=selected_artist_ids, genres=selected_genres_output)
            rec_counter=1
            rec_template = '{counter:>10}{track_title:<30}{artist_name:<30}{share_url:<50}'
            print(
                '\n',
                rec_template.format(counter=' ', track_title= 'Track Title', artist_name= 'Artist', share_url= 'URL'), 
                '\n', '-'*125
            )
            for track in recommendations:
                if len(track.get('name'))<=25:
                    rec_song=track.get('name')  
                else:
                    rec_song=track.get('name') [:25]+'...'

                if len(track.get('artist').get('name'))<=25:
                    rec_artist=track.get('artist').get('name')
                else:
                    rec_artist=track.get('artist').get('name')[:25]+'...'

                if len(track.get('share_url'))<=50:
                    rec_link=track.get('share_url')
                else:
                    rec_link=track.get('share_url')[:50]+'...'
                    
                print(
                    rec_template.format(counter=str(rec_counter)+'. ',track_title=rec_song, 
                    artist_name=rec_artist,share_url=rec_link)
                    )
                rec_counter+=1
                

        elif selected_genres_output==['none selected']: 
            recommendations=spotify.get_similar_tracks(artist_ids=selected_artist_ids)
            rec_counter=1
            rec_template = '{counter:>10}{track_title:<30}{artist_name:<30}{share_url:<50}'
            print(
                '\n',
                rec_template.format(counter=' ', track_title= 'Track Title', artist_name= 'Artist', share_url= 'URL'), 
                '\n', '-'*125
            )
            for track in recommendations:
                if len(track.get('name'))<=25:
                    rec_song=track.get('name')  
                else:
                    rec_song=track.get('name') [:25]+'...'

                if len(track.get('artist').get('name'))<=25:
                    rec_artist=track.get('artist').get('name')
                else:
                    rec_artist=track.get('artist').get('name')[:25]+'...'

                if len(track.get('share_url'))<=50:
                    rec_link=track.get('share_url')
                else:
                    rec_link=track.get('share_url')[:50]+'...'
                    
                print(
                    rec_template.format(counter=str(rec_counter)+'. ',track_title=rec_song, 
                    artist_name=rec_artist,share_url=rec_link)
                )
                rec_counter+=1
                

        elif not selected_artist_ids:
            recommendations=spotify.get_similar_tracks(genres=selected_genres_output)
            rec_counter=1
            rec_template = '{counter:>10}{track_title:<30}{artist_name:<30}{share_url:<50}'
            print(
                '\n',
                rec_template.format(counter=' ', track_title= 'Track Title', artist_name= 'Artist', share_url= 'URL'), 
                '\n', '-'*125
            )
            for track in recommendations:
                if len(track.get('name'))<=25:
                    rec_song=track.get('name')  
                else:
                    rec_song=track.get('name') [:25]+'...'

                if len(track.get('artist').get('name'))<=25:
                    rec_artist=track.get('artist').get('name')
                else:
                    rec_artist=track.get('artist').get('name')[:25]+'...'

                if len(track.get('share_url'))<=50:
                    rec_link=track.get('share_url')
                else:
                    rec_link=track.get('share_url')[:50]+'...'
                    
                print(
                    rec_template.format(counter=str(rec_counter)+'. ',track_title=rec_song, 
                    artist_name=rec_artist,share_url=rec_link)
                )
                rec_counter+=1
                
    except:
        print('Please choose up to 5 total artists and genres.')

    #while True:
    while len(selected_artists_output)+len(selected_genres_output)<=5:
        send_recommendations=input('Would you like to email this list to yourself or to a friend (y/n)?')
        if send_recommendations.lower()=='y':
            email_to=input('Who are you sending this to (separate multiple emails with a comma)?')
            email_to=email_to.split(',')
            email_from=input('What\'s your email address?')
            subject=input('Enter a subject for your email:')
            rec_list_html=spotify.get_formatted_tracklist_table_html(recommendations)
            sendgrid.send_mail(email_from, email_to, subject, rec_list_html)
            break
        elif send_recommendations.lower()=='n':
            break
        else:
            print('Please select "y" for yes or "n" for no.')
            continue

# Begin Main Program Loop:
while True:
    print_menu()
    choice = input('What would you like to do? ')
    if choice == '1':
        handle_genre_selection()
    elif choice == '2':
        handle_artist_selection()
    elif choice == '3':
        get_recommendations()
    elif choice == '4':
        print('Quitting...')
        break
    else:
        print(choice, 'is an invalid choice. Please try again.')
    print()
    input('Press enter to continue...')
