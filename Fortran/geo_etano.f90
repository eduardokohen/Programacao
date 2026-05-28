program optimize_ethane

    implicit none

    real(8) :: r
    real(8) :: r0
    real(8) :: k
    real(8) :: energy
    real(8) :: grad
    real(8) :: alpha
    integer :: i

    ! distância inicial C-C
    r = 2.0d0

    ! distância de equilíbrio
    r0 = 1.54d0

    ! constante de força
    k = 300.d0

    ! passo da otimização
    alpha = 0.001d0

    print *, "Iteração   Distância      Energia"

    do i = 1, 1000

        ! energia
        energy = 0.5d0 * k * (r - r0)**2

        ! gradiente dE/dr
        grad = k * (r - r0)

        ! atualização da geometria
        r = r - alpha * grad

        print *, i, r, energy

        ! critério de convergência
        if (abs(grad) < 1.0d-6) exit

    end do

    print *
    print *, "Geometria otimizada:"
    print *, "Distância C-C =", r

end program optimize_ethane