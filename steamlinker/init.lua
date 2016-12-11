function onTextMessageEvent(serverConnectionHandlerID, targetMode, toID, fromID, fromName, fromUniqueIdentifier, message)

			if string.find(string.lower(message), "store.steampowered.com/app/") then

			ts3.printMessageToCurrentTab("[URL=steam://store/"..string.gsub(string.match(message, '/....../'),"/","",2).."]Open in Steam.[/URL]")

		end
	return
end
