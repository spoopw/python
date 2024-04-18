import pytest
from television import Television


class TestTelevision:
    """
    A class that tests functions from television.py
    """

    def setup_method(self):
        self.tv = Television()
        self.tv2 = Television()

    def test___init__(self):
        assert self.tv.MIN_VOLUME == 0
        assert self.tv.MAX_VOLUME == 2
        assert self.tv.MIN_CHANNEL == 0
        assert self.tv.MAX_CHANNEL == 3

    def test_power(self):
        """
        Various tests for the power function
        """
        self.tv.power()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 0'
        self.tv.power()
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_mute(self):
        """
        Various tests for the mute function
        """
        self.tv.power()
        self.tv.volume_up()
        self.tv.mute()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 0'
        self.tv.mute()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 1'
        self.tv.power()
        self.tv.mute()
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 1'
        self.tv.mute()
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 1'

    def test_channel_up(self):
        """
        Various tests for the channel_up function
        """
        self.tv.channel_up()
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 0'
        self.tv.power()
        self.tv.channel_up()
        assert self.tv.__str__() == 'Power = True, Channel = 1, Volume = 0'
        self.tv.channel_up()
        assert self.tv.__str__() == 'Power = True, Channel = 2, Volume = 0'
        self.tv.channel_up()
        assert self.tv.__str__() == 'Power = True, Channel = 3, Volume = 0'
        self.tv.channel_up()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 0'

    def test_channel_down(self):
        """
        Various tests for the channel_down function
        """
        self.tv.channel_down()
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 0'
        self.tv.power()
        self.tv.channel_down()
        assert self.tv.__str__() == 'Power = True, Channel = 3, Volume = 0'

    def test_volume_up(self):
        """
        Various tests for the volume_up function
        """
        self.tv.volume_up()
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 0'
        self.tv.power()
        self.tv.volume_up()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 1'
        self.tv.mute()
        self.tv.volume_up()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 2'
        self.tv.volume_up()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 2'

    def test_volume_down(self):
        """
        Various tests for the volume_down function
        """
        self.tv.volume_down()
        assert self.tv.__str__() == 'Power = False, Channel = 0, Volume = 0'
        self.tv.power()
        #
        self.tv.volume_up()  # Changing volume to max to see how volume down works
        self.tv.volume_up()  # Changing volume to max to see how volume down works
        #
        self.tv.volume_down()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 1'
        self.tv.mute()
        self.tv.volume_down()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 0'
        self.tv.volume_down()
        assert self.tv.__str__() == 'Power = True, Channel = 0, Volume = 0'

    if __name__ == '__main__':
        pytest.main()
