# Genre Mixer
A playlist generator that creates Spotify playlists based on your desired genre.

# How does it work.

Genre Mixer communicates with Spotify's API to deliver playlists based on the user-specified parameters. In other words, Genre Mixer brings you a Spotify playlist based on what you asked it.

It utilizes BeautifulSoup to communicate with a website named everynoise.com. It uses this web-scraping tool to learn about various genres and the artists connected to them. With this information, it is able to connect with Spotify's web API to learn more about the genre and gather songs. From there, it uses them to curate a special playlist containing songs that fit the genre.

# Why I made this.

I am a passionate music listener; however, I am not a specialists when it comes to genres. I love to explore many genres as I can. This leads me to wanting an application that allows me to browse through various genres. However, there weren't a lot of apps on the market that offers this. There are wonderful websites and that that are catered to finding new music; However, I wanted a more powerful tool that let's me browse music without scouraging through random playlists and websites. It's through this problem that I come up with Genre Mixer.

# How to run it.

All you really need to do is run the main.py file. It might prompt you to sign in with your Spotify account credentials; this is done so the program is able to create the playlists in your account. With this in mind, you'll need to Spotify account for this to work.

# The Future.

I do plan on working on this more in the future. Right now, the website this program is using to gather data has been discontinued and no longer updating. Therefore, I may need to switch to a more supported platform to gather data. This could be an external API or another website that offers information on genres. Additionally, I plan to add frontend features to make the application more accessible. Overall, there is a lot of room to improve for this program, and I hope to make this program into a very useful tool for music lovers.
