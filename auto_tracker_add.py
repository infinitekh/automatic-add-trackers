#!/usr/bin/env kross
# -*- coding: utf-8 -*-
import KTorrent
import KTScriptingPlugin
import Kross
#from PyQt4 import QtCore

t = Kross.module("kdetranslation")

class AutoTrackerAdd:
	def __init__(self):
		KTorrent.connect("torrentAdded(const QString &)",self.torrentAdded)
		tors = KTorrent.torrents()
		# bind to signals for each torrent
		f= open(KTScriptingPlugin.scriptDir("auto_tracker_add") + "tracker.list")
		self.trackers=f.read().splitlines()		

		for t in tors:
			self.torrentAdded(t)
		
		
	
	def torrentAdded(self,ih):
		tor = KTorrent.torrent(ih)
		KTorrent.log("Torrent added %s" % tor.name())
		for tk in self.trackers:
			tor.addTracker(tk)

		
#	def save(self):
#		KTScriptingPlugin.writeConfigEntryBool("AutoTrackerAddScript","remove_on_finish_downloading",self.remove_on_finish_downloading)
#		KTScriptingPlugin.writeConfigEntryBool("AutoTrackerAddScript","remove_on_finish_seeding",self.remove_on_finish_seeding)
#		KTScriptingPlugin.syncConfig("AutoTrackerAddScript")
#	
#	def load(self):
#		self.remove_on_finish_downloading = KTScriptingPlugin.readConfigEntryBool("AutoTrackerAddScript","remove_on_finish_downloading",False)
#		self.remove_on_finish_seeding = KTScriptingPlugin.readConfigEntryBool("AutoTrackerAddScript","remove_on_finish_seeding",False)
#		
#	def configure(self):
#		forms = Kross.module("forms")
#		dialog = forms.createDialog(t.i18n("Auto Remove Settings"))
#		dialog.setButtons("Ok|Cancel")
#		page = dialog.addPage(t.i18n("Auto Remove"),t.i18n("Auto Remove"),"kt-remove")
#		widget = forms.createWidgetFromUIFile(page,KTScriptingPlugin.scriptDir("auto_tracker_add") + "auto_tracker_add.ui")
#		widget["finish_seeding"].checked = self.remove_on_finish_seeding
#		widget["finish_downloading"].checked = self.remove_on_finish_downloading
#		if dialog.exec_loop():
#			self.remove_on_finish_seeding = widget["finish_seeding"].checked 
#			self.remove_on_finish_downloading = widget["finish_downloading"].checked
#			self.save()
#

ata = AutoTrackerAdd()
#ar.load()

#def configure():
#	global ar
#	ar.configure()

def unload():
	global ata
	del ata
