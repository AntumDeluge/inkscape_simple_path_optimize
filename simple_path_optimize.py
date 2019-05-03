#!/usr/bin/env python

# This work is released under Creative Commons Zero (CC0).
#
# The author hereby waives all copyright and related or
# neighboring rights together with all associated claims
# and causes of action with respect to this work to the
# extent possible under the law.
#
# See: https://creativecommons.org/publicdomain/zero/1.0/legalcode

import inkex, os, subprocess, sys, tempfile, traceback

# in case run outside of Inkscape's extensions directory on Linux/Unix-like systems
sys.path.append('/usr/share/inkscape/extensions')


# helper function for calling inkscape commands
def execute(params=None):
	# verbs require GUI so cannot use '-z' paramater?
	#cmd = ['inkscape', '-z',]
	cmd = ['inkscape',]
	if sys.platform == 'win32':
		# support stdout on Windows
		cmd[0] = 'inkscape.com'

	if not params:
		params = cmd
	else:
		if type(params) == str:
			params = params.split(' ')
		elif type(params) == tuple:
			params = list(params)

		params = cmd + params

	proc = subprocess.Popen(params, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = proc.communicate()

	if err:
		# clean up error message
		err = err.strip(' \t\n\r')
		inkex.errormsg('Error: {}'.format(err))
		return

	# clean up output
	return out.strip(' \t\n\r')


# main class
class SimplePathOptimize(inkex.Effect):
	def __init__(self):
		inkex.Effect.__init__(self)

	def effect(self):
		selected = self.selected
		if not selected:
			inkex.errormsg('Please select object(s) for path optimization')
			return

		# create a temp SVG document
		temp_file = tempfile.mktemp('temp.svg')
		self.document.write(temp_file)

		# get all selected paths for selection in temp document
		cmd_list = []
		for S in selected:
			cmd_list.append('--select={}'.format(S))

		verb_list = (
			'SelectionCombine',
			'SelectionUnion',
			'SelectionSimplify',
			'SelectionBreakApart',
			'FileSave',
			'FileQuit',
			)

		for V in verb_list:
			cmd_list.append('--verb={}'.format(V))

		cmd_list += ['-f', temp_file]
		execute(cmd_list)

		# get results
		BUFFER = open(temp_file, 'r')
		new_document = inkex.etree.parse(BUFFER)
		BUFFER.close()

		# delete temporary file
		try:
			os.remove(temp_file)
		except:
			msg = 'Error removing temporary file: {}\n\n'.format(temp_file)
			msg += traceback.format_exc()

			# clean up message
			msg = msg.strip(' \t\n\r')

			inkex.errormsg(msg)

		# update open document
		self.document = new_document


if __name__ == '__main__':
	SimplePathOptimize().affect()
