import sublime, sublime_plugin
import time

class TimeSmurfCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		tFormat = self.view.settings().get('timesmurf_formatstring')
		tString = time.strftime(tFormat)
		pos = self.view.sel()
		for caret in pos:
			index = caret.begin()
			self.view.insert(edit, index, tString)

