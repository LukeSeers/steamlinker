function onTextMessageEvent(serverConnectionHandlerID, targetMode, toID, fromID, fromName, fromUniqueIdentifier, message, ffIgnored)


	-- Steam Store
	if string.find(string.lower(message), "store.steampowered.com/app/") then

		ts3.printMessageToCurrentTab("[URL=steam://store/"..string.gsub(string.match(message, '%d+'),"/","",2).."]Open in Steam.[/URL]")

		end

	-- Profile SteamID64
	if string.find(string.lower(message), "steamcommunity.com/profiles/") then

		ts3.printMessageToCurrentTab("[URL=steam://openurl/https://steamcommunity.com/profiles/"..string.gsub(string.match(message, '%d+'),"/","",2).."]Open in Steam.[/URL]")

		end

	-- Profile CustomURL
	if string.find(string.lower(message), "steamcommunity.com/id/") then

		ts3.printMessageToCurrentTab("[URL="..string.sub(""..string.gsub(""..message.."", "http://", "steam://openurl/http://").."", 6, -7).."]Open in Steam.[/URL]")

		end

	-- Steam workshop (FrontPage)
	if string.find(string.lower(message), "steamcommunity.com/app/") then

		ts3.printMessageToCurrentTab("[URL="..string.sub(""..string.gsub(""..message.."", "http://", "steam://openurl/http://").."", 6, -7).."]Open in Steam.[/URL]")

		end

	 -- Steam Workshop (AddonPage)
	 if string.find(string.lower(message), "steamcommunity.com/sharedfiles/filedetails/") then

		ts3.printMessageToCurrentTab("[URL="..string.sub(""..string.gsub(""..message.."", "http://", "steam://openurl/http://").."", 6, -7).."]Open in Steam.[/URL]")

		end

	 -- Steam Discussions (Forum)
	 if string.find(string.lower(message), "steamcommunity.com/discussions/") then

		 ts3.printMessageToCurrentTab("[URL="..string.sub(""..string.gsub(""..message.."", "http://", "steam://openurl/http://").."", 6, -7).."]Open in Steam.[/URL]")

		 end

	 -- Steam Groups
	 if string.find(string.lower(message), "steamcommunity.com/groups/") then

		ts3.printMessageToCurrentTab("[URL="..string.sub(""..string.gsub(""..message.."", "http://", "steam://openurl/http://").."", 6, -7).."]Open in Steam.[/URL]")

		

	return
end



