program zpe_ethane
    implicit none

    integer :: i
    real(8) :: zpe
    real(8), parameter :: hartree_conv = 219474.6313705d0

    real(8), dimension(18) :: freq = (/ &
        289.32d0, &
        822.72d0, 822.72d0, &
        995.11d0, &
        1195.3d0, 1195.3d0, &
        1379.16d0, &
        1397.d0, &
        1468.1d0, 1468.1d0, &
        1472.03d0, 1472.03d0, &
        2895.67d0, &
        2954.d0, &
        2968.69d0, 2968.69d0, &
        2985.39d0, 2985.39d0 /)

    zpe = 0.d0

    do i = 1, 18
        zpe = zpe + 0.5d0 * freq(i)
    end do

    zpe = zpe / hartree_conv

    print *, "ZPE (Hartree): ", zpe

end program zpe_ethane