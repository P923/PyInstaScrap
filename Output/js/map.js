
    epsg4326 = new OpenLayers.Projection("EPSG:4326")

    map = new OpenLayers.Map({
      div: "DivMappa",
      displayProjection: epsg4326   // With this setting, lat and lon are displayed correctly in MousePosition and permanent anchor
    });

    map.addLayer(new OpenLayers.Layer.OSM());

    map.addControls([
      new OpenLayers.Control.MousePosition(),
      new OpenLayers.Control.ScaleLine(),
      new OpenLayers.Control.LayerSwitcher(),
      new OpenLayers.Control.Permalink({ anchor: true })
    ]);

    projectTo = map.getProjectionObject(); //The map projection (Spherical Mercator)
    var lonLat = new OpenLayers.LonLat(markers[0][0], markers[0][1]).transform(epsg4326, projectTo);
    var zoom = 6;
    if (!map.getCenter()) {
      map.setCenter(lonLat, zoom);
    }


    var colorList = ["red", "blue", "yellow"];
    var layerName = [markers[0][2]];
    var styleArray = [new OpenLayers.StyleMap({ pointRadius: 6, fillColor: colorList[0], fillOpacity: 0.5 })];
    var vectorLayer = [new OpenLayers.Layer.Vector(layerName[0], { styleMap: styleArray[0] })];		// First element defines first Layer

    var j = 0;
    for (var i = 1; i < markers.length; i++) {
      if (!layerName.includes(markers[i][2])) {
        j++;
        layerName.push(markers[i][2]);															// If new layer name found it is created
        styleArray.push(new OpenLayers.StyleMap({ pointRadius: 6, fillColor: colorList[j % colorList.length], fillOpacity: 0.5 }));
        vectorLayer.push(new OpenLayers.Layer.Vector(layerName[j], { styleMap: styleArray[j] }));
      }
    }

    for (var i = 0; i < markers.length; i++) {
      var lon = markers[i][0];
      var lat = markers[i][1];
      var feature = new OpenLayers.Feature.Vector(
        new OpenLayers.Geometry.Point(lon, lat).transform(epsg4326, projectTo),
        { description: "marker number " + i }
      );
      vectorLayer[layerName.indexOf(markers[i][2])].addFeatures(feature);
    }

    for (var i = 0; i < layerName.length; i++) {
      map.addLayer(vectorLayer[i]);
    }

