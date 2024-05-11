import flet as ft # Library to make code for web, mobile e desktop
def main(page): # Function to create the main page
     page.title = 'Hashzap' # Set the title of the page

     title = ft.Text('Hashzap') # Create a text element
     page.add(title) # Add the element to the page

     def startChat(event): # Do something when the button is clicked
          page.dialog = poupUp # Show the dialog
          poupUp.open = True # Open the dialog
          page.update() # Update the page


     button_start = ft.ElevatedButton('Iniciar', on_click=startChat) # Create a button element
     page.add(button_start) # Add the element to the page

     def enter_chat(event): # Do something when the button is clicked
          sender = field_name.value
          page.remove(title) # Remove the element from the page
          page.remove(button_start)
          poupUp.open = False # Close the dialog
          page.add(chat, row_message) # Add the element to the page
          page.pubsub.send_all(f'{sender} entrou no chat.') # Add the element to the page
          page.update()

     title_poupUp = ft.Text('Bem vindo ao Hashzap') # Create a text element
     field_name = ft.TextField(label='Escreva seu nome', on_submit=enter_chat) # Create a text field element
     enter_chat_button = ft.ElevatedButton('Entrar no chat', on_click=enter_chat) # Create a button element
          
     poupUp = ft.AlertDialog(title=title_poupUp, content=field_name, actions=[enter_chat_button]) # Create a alert dialog element

     def message_socket(mensagem): # Create a way to everyone see the message
          new_message = ft.Text(mensagem) # Create a text element
          chat.controls.append(new_message) # Add the element to the page
          page.update() # Update the page
     page.pubsub.subscribe(message_socket) # Subscribe to the way of communiction

     def sendMessage(event): # Do something when the button is clicked
          sender = field_name.value # Name of the sender
          message = text_chat.value  # Message to be sent
          page.pubsub.send_all(f'{sender}: {message}') # Send the message to all users
          text_chat.value = ''
          page.update()

     chat = ft.Column()
     text_chat = ft.TextField(label='Digite sua mensagem', on_submit=sendMessage)
     button_send_message = ft.ElevatedButton('Enviar', on_click=sendMessage)
     row_message = ft.Row([text_chat, button_send_message])

ft.app(main, view=ft.WEB_BROWSER, port=64669) # Start the app (web, mobile e desktop) with the main page