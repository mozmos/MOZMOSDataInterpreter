# MOZMOSDataInterpreter
An interactive GUI for loading and analysing data collected from the MOZMOS Data Collection Module

## Legal
MOZMOS Data Interpreter, and accompanying software, documentation and files are products of the MOZMOS Entity, and the legal property of such. Any illicit use, such as pirating, cracking or otherwise unpermissed use of the software is illegal under copyright law and the EULA.

## Current Features
* Load data straight from SD Card into the program
* Individually view different data types
* Automatically plots the datapoints along a line graph, with colouring and labels
* You can save these graphs as a .png file

## Latest Update - Version 0.1.4
* Introducing a settings menu!
    * 5 new themes for the graph to add flair
        * _Light Theme - A default theme, suitable for presentations and office meetings_
        * _Dark Theme - A darker theme for more modernistic feels_
        * _Desert Theme - A stylised theme for more specific applications_
        * _Oceanic Theme - An ocean-based theme, perfect for what MOZMOS is related to_
        * _MOZ-Theme - A custom theme based on the MOZMOS Colour Pallete_
    * Graph, Accessibility and Language content will be added in future updates
* Modular fashion for theme changing
* Themes are applied when saving images
* General bug fixes

## Future Features
- [ ] Settings Menu
    - [x] _Change colours_
    - [ ] _Change graph colours_
    - [ ] _Change graph type_
    - [ ] _Disability/Inclusivity Settings_
        - [ ] _Audio sounds for buttons and text_
    - [ ] _Change Language_
- [x] Graph Creation
- [x] Convert graph into image for exportation
- [ ] Options for image type when exporting graph
- [ ] Remove anti-override feature of graph saving
- [ ] Visually appealing interface
    - [ ] _Backgrounds_
    - [x] _Colours_
    - [ ] _Styles_
    - [x] _Buttons_
    
## Update List

<details>
   <summary>Click to expand</summary>
   
   #### Version 0.1.4
   * Introducing a settings menu!
    * 5 new themes for the graph to add flair
        * _Light Theme - A default theme, suitable for presentations and office meetings_
        * _Dark Theme - A darker theme for more modernistic feels_
        * _Desert Theme - A stylised theme for more specific applications_
        * _Oceanic Theme - An ocean-based theme, perfect for what MOZMOS is related to_
        * _MOZ-Theme - A custom theme based on the MOZMOS Colour Pallete_
    * Graph, Accessibility and Language content will be added in future updates
   * Modular fashion for theme changing
   * Themes are applied when saving images
   * General bug fixes

   #### Version 0.1.3
   * You can now save graphs as an image
   * Saved image's file name correlates to the type of data being shown
    * _Note that if there is an image with the identical name, it will override it_
   * Added stylised buttons and better spacing for a more intuitive user interface
    * _Buttons are now disabled before uploading data to prevent blank graphs from appearing
    * _Download Image button does not appear until data has been uploaded_
   * Graph will automatically update with the filtered data, including retaining the same colour for a more detailed look
   * Added automatic labelling of data points
   * General bug fixes

   #### Version 0.1.2
   * Created algorithm to generate graphs based on data
    * _Uses time as the x-axis, and the actual data points for the y-axis_
   * Embedded the graph into the TKinter software, so it will be manipulatable.
   * Graph algorithm automatically discerns between data types, and will colour and label each line accordingly
   * General Bug Fixes

   #### Version 0.1.1
   * Created the main GUI page
   * Created the algorithm to import the file, and backup systems in case something goes wrong with the import (including if something goes wrong)
   * Created stub buttons for data filtering
   * Created algorithm to read the data, and filter out any excess data so it can be cleanly split into groups of 4 (1 array position per data), and added these groups into a multi-dimensional array

</details>


## Hotfix list
<details>
   <summary>Click to expand</summary>
   
   #### Version 0.1.3
   * Hotfix 1: Fixed bug where uploading a second file would raise an error, and graph wouldn't display
   * Hotfix 2: Fixed bug where system would raise an error when data was already uploaded and user would cancel a second upload of data

</details>
