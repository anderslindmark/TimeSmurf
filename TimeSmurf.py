import sublime, sublime_plugin
from datetime import datetime

class TimeSmurfCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		tString = datetime.now().strftime('%Y-%m-%d %H:%M')
		pos = self.view.sel()
		for caret in pos:
			index = caret.begin()
			self.view.insert(edit, index, tString)

