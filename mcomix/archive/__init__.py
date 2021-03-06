# -*- coding: utf-8 -*-

import gtk

def ask_for_password():
    """ Openes an input dialog to ask for a password. Returns either
    an Unicode string (the password), or None."""
    dialog = gtk.MessageDialog(None, gtk.DIALOG_MODAL,
            gtk.MESSAGE_QUESTION, gtk.BUTTONS_OK_CANCEL)
    dialog.set_markup('<span weight="bold" size="larger">'
            + _("The archive is password-protected.")
            + '</span>')
    dialog.format_secondary_markup(_("Please enter the password to continue:"))
    dialog.set_default_response(gtk.RESPONSE_OK)
    password_box = gtk.Entry()
    password_box.set_visibility(False)
    password_box.set_activates_default(True)
    dialog.get_content_area().pack_end(password_box)
    dialog.set_focus(password_box)
    dialog.show_all()
    result = dialog.run()
    password = password_box.get_text()
    dialog.destroy()

    if result == gtk.RESPONSE_OK and password:
        return password.decode('utf-8')
    else:
        return None

# vim: expandtab:sw=4:ts=4
