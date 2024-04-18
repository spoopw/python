class Television:
    """
    Class for the television
    """
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self):
        """
        Declares self variables
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self):
        """
        Changes the power to on or off depending on self.__status
        """
        if not self.__status:
            self.__status = True
        else:
            self.__status = False

    def mute(self):
        """
        Mutes or unmutes the TV
        """
        if self.__status:
            if not self.__muted:
                self.__muted = True
            else:
                self.__muted = False

    def channel_up(self):
        """
        Changes the channel up by 1. If exceeding the max channel, wraps around to the min channel
        """
        if self.__status:
            self.__channel += 1
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        """
        Changes the channel down by 1. If exceeding the min channel, wraps around to the max channel
        """
        if self.__status:
            self.__channel -= 1
            if self.__channel < Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        """
        Changes the volume up by 1. If exceeding the max volume, sets volume to max volume
        """
        if self.__status:
            self.__volume += 1
            if self.__volume > Television.MAX_VOLUME:
                self.__volume = Television.MAX_VOLUME
            self.__muted = False

    def volume_down(self):
        """
        Changes the volume down by 1. If exceeding the min volume, sets volume to min volume
        """
        if self.__status:
            self.__volume -= 1
            if self.__volume < Television.MIN_VOLUME:
                self.__volume = Television.MIN_VOLUME
            self.__muted = False

    def __str__(self):
        """
        Changes the print statement to a specific format
        """
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
