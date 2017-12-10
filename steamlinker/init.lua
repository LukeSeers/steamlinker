function onTextMessageEvent(serverConnectionHandlerID, targetMode, toID, fromID, fromName, fromUniqueIdentifier, message, ffIgnored)

		if string.find(string.lower(message), "store.steampowered.com/app/") then

				ts3.printMessageToCurrentTab("[URL=steam://store/"..string.gsub(string.match(message, '%d+'),"/","",2).."]Open in Steam.[/URL]")

				end

		if string.find(string.lower(message), "steamcommunity.com/profiles/") then

				ts3.printMessageToCurrentTab("[URL=steam://openurl/https://steamcommunity.com/profiles/"..string.gsub(string.match(message, '%d+'),"/","",2).."]Open in Steam.[/URL]")

				end

		if string.find(string.lower(message), "steamcommunity.com/id/") then

				ts3.printMessageToCurrentTab("[URL="..string.sub(""..string.gsub(""..message.."", "http://", "steam://openurl/http://").."", 6, -7).."]Open in Steam.[/URL]")

				end

	return
end


