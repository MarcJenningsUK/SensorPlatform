<!doctype html>
<html class="no-js" lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Crimson Guitars Sensor Platform</title>
    <link rel="stylesheet" href="css/foundation.css">
    <link rel="stylesheet" href="css/app.css">
  </head>
  <body>
    <div class="row">
      <div class="large-12 columns">
        <h1>Crimson Guitars Sensor Platform</h1>
      </div>
    </div>

    <?php
	$filename = "/home/pi/SensorPlatform/configuration.conf";

        echo('<div class="row"><div class="large-12 columns"><div class="callout">');

	$myfile = fopen($filename, "c+") or die("Unable to open file!");
	while(!feof($myfile)) {
		$line = fgets($myfile);
		$splitLine = explode(":", $line, 2);

		if(count($splitLine) == 2)
		{
			$$splitLine[0] = $splitLine[1];
		}
	}
	fclose($myfile);

	if($_SERVER['REQUEST_METHOD'] == 'POST')
	{
		$myfile = fopen($filename, "w") or die("Unable to open file!");
		fwrite($myfile, "[default]\n");
		foreach ($_POST as $name => $val)
		{	
			$txt = htmlspecialchars($name . ':' . $val) . "\n";
			$output .= htmlspecialchars($name . ':' . $val) . "\n";
			fwrite($myfile, $txt);
		}
		fclose($myfile);

                echo('<p>Data written to the configuration file</p><pre>');
		echo($output);
		echo('</pre></div></div></div>');
	}
    ?>

    <div class="row">
      <div class="large-12 columns">
        <div class="callout">
          <h3>Configuration</h3>
          <p>You can set most of the configuration parameters for the platform in this page.</p>
        </div>
      </div>
    </div>

        <form data-abide method="post">
    <div class="row">
      <div class="large-8 medium-8 columns">
        <div class="row">
          <div class="large-12 columns">
            <div class="primary callout">
              <h5>Polling interval</h5>
              <label>Get readings every</label>
              <select name="frequency">
                <option value="30">30 seconds</option>
                <option value="60">1 minute</option>
                <option value="120" selected>2 minutes</option>
                <option value="300">5 minutes</option>
                <option value="18000">30 minutes</option>
              </select>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="large-12 columns">
            <div class="primary callout">
              <h5>Reporting</h5>
              <label>The URL to which data will be logged.</label>
              <input type="text" name="reportUrl" placeholder="large-12.columns" value="<?php echo $reportUrl; ?>" />
              <p><em>[temp]</em> will be replaced with the temperature value.<br />
              <em>[hum]</em> will be replaced with the humidity value.</p>
            </div>
          </div>
        </div>
        
        <div class="row">
          <div class="large-6 medium-6 columns">
            <div class="primary callout">
              <h5>Temperature</h5>
              <label>Trigger heating below</label>
              <input name="ttrigger" value=<?php echo $ttrigger; ?> type="number" placeholder="&deg;C" required pattern="[0-9.]"/>
              
              <label>Turn off above</label>
              <input name="ttriggerreset" value=<?php echo $ttriggerreset; ?> type="number" placeholder="&deg;C" />
              
              <label>Generate Warning below</label>
              <input name="twarning" value=<?php echo $twarning; ?> type="number" placeholder="&deg;C" />
              
            </div>
          </div>
          <div class="large-6 medium-6 columns">
            <div class="primary callout">
              <h5>Humidity</h5>
              <label>Trigger dehumidifier above</label>
              <input name="htrigger" value=<?php echo $htrigger; ?> type="number" placeholder="% Humidity" value="50" />
              
              <label>Turn off below</label>
              <input name="htriggerreset" value=<?php echo $htriggerreset; ?> type="number" placeholder="% Humidity" />
              
              <label>Generate Warning above</label>
              <input name="hwarning" value=<?php echo $hwarning; ?> type="number" placeholder="% humidity" />
              
            </div>
          </div>
        </div>
        
        <div class="row">
          <div class="large-4 medium-4 small-4 columns">
            <div class="primary callout">
              <p>Four columns</p>
            </div>
          </div>
          <div class="large-4 medium-4 small-4 columns">
            <div class="primary callout">
              <p>Four columns</p>
            </div>
          </div>
          <div class="large-4 medium-4 small-4 columns">
            <div class="primary callout">
              <p>Four columns</p>
            </div>
          </div>
        </div>

        <input type="submit" value="Save changes" class="success button">
        <input type="cancel" value="Undo changes" class="alert button">

        </form>

        <hr />

        <h5>We bet you&rsquo;ll need a form somewhere:</h5>
        <form>
          <div class="row">
            <div class="large-12 columns">
              <label>Input Label</label>
              <input type="text" placeholder="large-12.columns" />
            </div>
          </div>
          <div class="row">
            <div class="large-4 medium-4 columns">
              <label>Input Label</label>
              <input type="text" placeholder="large-4.columns" />
            </div>
            <div class="large-4 medium-4 columns">
              <label>Input Label</label>
              <input type="text" placeholder="large-4.columns" />
            </div>
            <div class="large-4 medium-4 columns">
              <div class="row collapse">
                <label>Input Label</label>
                <div class="input-group">
                  <input type="text" placeholder="small-9.columns" class="input-group-field" />
                  <span class="input-group-label">.com</span>
                </div>
              </div>
            </div>
          </div>
          <div class="row">
            <div class="large-12 columns">
              <label>Select Box</label>
              <select>
                <option value="husker">Husker</option>
                <option value="starbuck">Starbuck</option>
                <option value="hotdog">Hot Dog</option>
                <option value="apollo">Apollo</option>
              </select>
            </div>
          </div>
          <div class="row">
            <div class="large-6 medium-6 columns">
              <label>Choose Your Favorite</label>
              <input type="radio" name="pokemon" value="Red" id="pokemonRed"><label for="pokemonRed">Radio 1</label>
              <input type="radio" name="pokemon" value="Blue" id="pokemonBlue"><label for="pokemonBlue">Radio 2</label>
            </div>
            <div class="large-6 medium-6 columns">
              <label>Check these out</label>
              <input id="checkbox1" type="checkbox"><label for="checkbox1">Checkbox 1</label>
              <input id="checkbox2" type="checkbox"><label for="checkbox2">Checkbox 2</label>
            </div>
          </div>
          <div class="row">
            <div class="large-12 columns">
              <label>Textarea Label</label>
              <textarea placeholder="small-12.columns"></textarea>
            </div>
          </div>
        </form>
      </div>

      <div class="large-4 medium-4 columns">
        <h5>Try one of these buttons:</h5>
        <p><a href="#" class="button">Simple Button</a><br/>
        <a href="#" class="success button">Success Btn</a><br/>
        <a href="#" class="alert button">Alert Btn</a><br/>
        <a href="#" class="secondary button">Secondary Btn</a></p>
        <div class="callout">
          <h5>So many components, girl!</h5>
          <p>A whole kitchen sink of goodies comes with Foundation. Check out the docs to see them all, along with details on making them your own.</p>
          <a href="http://foundation.zurb.com/sites/docs/" class="small button">Go to Foundation Docs</a>
        </div>
      </div>
    </div>
    
    
    <div class="row">
      <div class="large-12 columns">
        <p>&copy; 2017 Marc Jennings.  All rights reserved.</p>
      </div>
    </div>

    <script src="js/vendor/jquery.js"></script>
    <script src="js/vendor/what-input.js"></script>
    <script src="js/vendor/foundation.js"></script>
    <script src="js/app.js"></script>
  </body>
</html>
