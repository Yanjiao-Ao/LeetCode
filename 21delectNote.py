def delectNote(note):#listnote
    note.val = note.next.val
    note.next.next = note.next
