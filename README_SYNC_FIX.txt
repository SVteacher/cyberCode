CyberGrader.io Sync Fix Package
=================================

What this fixes
---------------
- Restores Session Cache
- Restores Save to Cache buttons
- Adds Export Device Data
- Adds Import Device Data
- Keeps Save Override device-local behavior
- Lets you move overrides + cache between devices manually using a JSON file

How to use
----------
1. Replace your GitHub repo's current index.html with this index.html
2. Commit changes
3. Refresh the site after GitHub Pages republishes

Cross-device workflow
---------------------
- On one device, use Export Device Data
- Save the JSON file
- On another device, use Import Device Data
- Your overrides and cache will load there

Important
---------
This is not automatic cloud sync. It is a no-cost manual sync that works with a static GitHub Pages site.
