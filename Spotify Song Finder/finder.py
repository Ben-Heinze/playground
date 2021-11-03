import csv


#==================================================================================================
def returned_list(filename, playlist):  #takes playlist and returns it as a list
    with open(filename, 'r', encoding="utf8") as data:
        file = csv.reader(data, delimiter= ',', lineterminator='\n')
        song_Bank = []
        for line in file:
            if line[3] == playlist:
                song_info = [line[0],line[1]]
                song_Bank.append(song_info)
            else:
                continue
    data.close()
    return song_Bank  #Returns tuple of songBank and count  #should return 866      
#==================================================================================================
def new_PL_compare(filename, playlist,returned_list, save_as):
    with open(filename, 'r', encoding="utf8") as data:  #encoding fixes unknown characters in csv
        small_PL = csv.reader(data, delimiter= ',', lineterminator='\n')    #turns each line into simple list
        outfile = open(save_as, 'w', encoding="utf8")
        similarity_check = 0
        line_count = 0

        for line in small_PL:
            if line[3] == playlist:
                line_count +=1
                song = [line[0],line[1]]
                if song in returned_list:   #if the song IS in my playlist:
                    similarity_check +=1
                else:                       #if the song is NOT in my current playlist:
                    outfile.write(str(song)+ str(line_count) + '\n')
            else:
                continue


        accuracy = (similarity_check/line_count)
        print("Similarity: " , str(accuracy) + "%")
                
                    

                
    outfile.close() 
    data.close()
                                                       # splitted_list = file.split(',')
      #  for line in file:
     #       count +=1
     #       print(line, count)
                
#==================================================================================================
def get_file(save_as, returned_tuple):
    outfile = (save_as, 'w')

    song_list, total_count = returned_tuple
    type(song_list)

    for song in list(song_list):
        print(song)
       # song0 = str(song)
        output = "Title: " + str(song[0]) + "Artist: " + str(song[1])
        outfile.write(output)
    outfile.close()



def song_finder(old, new):
    pass


#-----------------------------------------------------------------------------------------------
def main(old_filename, new_filename):
    #playlist = input("Choose a playlist to compare: ")
    playlist = "Something"

    big_PL = returned_list(new_filename, playlist)
    new_PL_compare(old_filename,playlist, big_PL,"missing songs.txt")
    

    



        
    


main("Spotify_playlist_as_of_Dec._10_2020.csv","My_Spotify_Playlist.csv")
