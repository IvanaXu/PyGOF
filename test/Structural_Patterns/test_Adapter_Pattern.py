# -*- coding:utf-8 -*-
# @auth ivan
# @time 2016-10-14 10:54:35
# @goal test Adapter Pattern 


class AdvancedMediaPlayer:
    def __init__(self):
        return

    def playVlc(self):
        return

    def playMP4(self):
        return


class VlcPlayer(AdvancedMediaPlayer):
    def __init__(self, fileName):
        AdvancedMediaPlayer.__init__(self)
        self.fileName = fileName
        return

    def playVlc(self):
        print "Playing vlc file. Name: " + self.fileName

    def playMP4(self):
        return
# A = VlcPlayer('1')
# A.playVlc()
# A.playMP4()


class Mp4Player(AdvancedMediaPlayer):
    def __init__(self, fileName):
        AdvancedMediaPlayer.__init__(self)
        self.fileName = fileName
        return

    def playVlc(self):
        return

    def playMP4(self):
        print "Playing mp4 file. Name: " + self.fileName


class MediaPlayer:
    def __init__(self):
        return

    def play(self):
        return


class MediaAdapter(MediaPlayer):
    def __init__(self, audioType, fileName):
        MediaPlayer.__init__(self)
        self.audioType, self.fileName = audioType, fileName
        # self.advancedMusicPlayer = AdvancedMediaPlayer()

        if self.audioType == "vlc":
            self.advancedMusicPlayer = VlcPlayer(self.fileName)
        elif self.audioType == "mp4":
            self.advancedMusicPlayer = Mp4Player(self.fileName)
        return

    def play(self):
        if self.audioType == "vlc":
            self.advancedMusicPlayer.playVlc()
        elif self.audioType == "mp4":
            self.advancedMusicPlayer.playMP4()
        return


class AudioPlayer(MediaPlayer):
    def __init__(self, audioType, fileName):
        MediaPlayer.__init__(self)
        self.audioType, self.fileName = audioType, fileName

        self.mediaAdapter = MediaAdapter(self.audioType, self.fileName)
        return

    def play(self):
        if self.audioType == "mp3":
            print "Playing mp3 file. Name: " + self.fileName
        elif self.audioType == "vlc" or self.audioType == "mp4":
            self.mediaAdapter.play()
        else:
            print "Invalid media. " + self.audioType + " format not supported"


class AdapterPatternDemo:
    def __init__(self):
        play_list = [
            ("mp3", "beyond the horizon.mp3"),
            ("mp4", "alone.mp4"),
            ("vlc", "far far away.vlc"),
            ("avi", "mind me.avi"),
                     ]
        for i in play_list:
            (self.audioType, self.fileName) = i
            self.audioPlayer = AudioPlayer(self.audioType, self.fileName)
            self.audioPlayer.play()

AdapterPatternDemo()

