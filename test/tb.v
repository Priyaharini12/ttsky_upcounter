`default_nettype none
`timescale 1ns / 1ps

module tb ();

  // Dump waveform
  initial begin
    $dumpfile("tb.fst");
    $dumpvars(0, tb);
  end

  // Inputs
  reg clk;
  reg rst_n;
  reg ena;
  reg [7:0] ui_in;
  reg [7:0] uio_in;

  // Outputs
  wire [7:0] uo_out;
  wire [7:0] uio_out;
  wire [7:0] uio_oe;

`ifdef GL_TEST
  wire VPWR = 1'b1;
  wire VGND = 1'b0;
`endif

  // Instantiate DUT
  tt_um_example user_project (

`ifdef GL_TEST
      .VPWR(VPWR),
      .VGND(VGND),
`endif

      .ui_in   (ui_in),
      .uo_out  (uo_out),
      .uio_in  (uio_in),
      .uio_out (uio_out),
      .uio_oe  (uio_oe),
      .ena     (ena),
      .clk     (clk),
      .rst_n   (rst_n)
  );

  // Clock generation
  always #5 clk = ~clk;

  // Test sequence
  initial begin
    clk    = 0;
    rst_n  = 0;     // Active low reset
    ena    = 1;
    ui_in  = 8'b0;
    uio_in = 8'b0;

    // Hold reset for some time
    #10;
    rst_n = 1;

    // Run simulation
    #100;

    $finish;
  end

  // Monitor output
  initial begin
    $monitor("Time = %0t | rst_n = %b | Count = %d",
              $time, rst_n, uo_out[3:0]);
  end

endmodule

`default_nettype wire
