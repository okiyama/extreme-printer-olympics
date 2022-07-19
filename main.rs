struct BmpHeader {
    header: u16, //Always 0x42 0x4D
    filesize: u32,
    reserved1: u16,
    reserved2: u16,
    image_data_offset: u32,

    size_of_header: u32, //always 40
    width: u32,
    height: u32,
	number_of_color_planes: u16, //always 1

	bit_per_pixel: u16, //Typical values are 1, 4, 8, 16, 24 and 32
	compression_method: u32,
	image_size: u32,
	horizontal_resolution: u32, //the horizontal resolution of the image. (pixel per metre, signed integer)
	vertical_resolution: u32, //the vertical  resolution of the image. (pixel per metre, signed integer)

	colors_in_palette: u32, //the number of colors in the color palette, or 0 to default to 2n
	important_colors: u32, //the number of important colors used, or 0 when every color is important, generally ignored
}


fn main() {
	const width: u32 = 600;
	const height: u32 = 2400;
	let pixel_data: [u8; 3 * width * height];
	const black_pixel: [u8; 3] = [255, 255, 255];
	let mut current_width = 1;

  //   let header = BmpHeader {
  //   	header: 0x424D,
  //  		filesize: ,
  //   	reserved1: ,
  //   	reserved2: ,
  //   	image_data_offset: ,
  //   	size_of_header: ,
  //   	width: ,
  //   	height: ,
		// number_of_color_planes: ,
		// bit_per_pixel: ,
		// compression_method: ,
		// image_size: ,
		// horizontal_resolution: ,
		// vertical_resolution: ,
		// colors_in_palette: ,
		// important_colors: ,
  //   }
}