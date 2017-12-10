import random


class Player:
	_herd = []
	_start = [3, 3, 3]
	_enemy = []
	_started = False

	def __init__(self):
		for i in range(0, 6):
			self._herd.append(6)

	def send_number(self):
		pass

	def reinit(self):
		print('Re-stock')
		for i in range(0, 6):
			self._herd[i] = 6

	def get_number(self):
		if len(self._start) > 0:
			_n = self._start.pop()
			print('Sending start: {}'.format(_n + 1))
		else:
			_n = random.randint(0, 5)
			while self._herd[_n] <= 0:
				_n = random.randint(0, 5)
			print('Sending next: {}'.format(_n + 1))

		self._herd[_n] -= 1

		has_more = False
		for i in range(0, 6):
			if self._herd[i] > 0:
				has_more = True
				break
		if not has_more:
			self.reinit()

		return _n + 1
