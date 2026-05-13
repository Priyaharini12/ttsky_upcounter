`default_nettype none
`timescale 1ns / 1ps

module tb;

  // =========================
  // Dump waveform
  // =========================
  initial begin
    $dumpfile("tb.fst");
    $dumpvars(0, tb);
  end

  // =========================
  // Inputs
  // =========================
  reg clk;
  reg rst_n;
  reg ena;
  reg [7:0] ui_in;
  reg [7:0] uio_in;

  // =========================
  // Outputs
  // =========================
  wire [7:0] uo_out;
  wire [7:0] uio_out;
  wire [7:0] uio_oe;

`ifdef GL_TEST
  wire VPWR = 1'b1;
  wire VGND = 1'b0;
`endif

  // =========================
  // DUT Instantiation
  // =========================
  tt_um_example user_project (

`ifdef GL_TEST
      .VPWR   (VPWR),
      .VGND   (VGND),
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

  // =========================
  // Clock generation
  // =========================
  initial clk = 0;

  always #5 clk = ~clk;

  // =========================
  // Test sequence
  // =========================
  initial begin

    // Initialize inputs
    rst_n  = 0;
    ena    = 1'b1;
    ui_in  = 8'b00000000;
    uio_in = 8'b00000000;

    // Hold reset
    #20;
    rst_n = 1;

    // Run simulation long enough
    #200;

    // PASS message
    $display("TEST COMPLETED SUCCESSFULLY");

    // End simulation
    $finish;
  end

  // =========================
  // Monitor
  // =========================
  initial begin
    $monitor("Time = %0t | rst_n = %b | Count = %0d",
              $time, rst_n, uo_out[3:0]);
  end

endmodule

`default_nettype wire
